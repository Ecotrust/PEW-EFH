# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
import json as simplejson
from django.views.decorators.cache import cache_page
from .models import *


#@cache_page(60 * 60 * 24, key_prefix="data_manager_get_json")
def get_json(request, project=None):
    from mp_settings.models import *
    try:
        if project:
            activeSettings = MarinePlannerSettings.objects.get(slug_name=project)
        else:
            activeSettings = MarinePlannerSettings.objects.get(active=True)

        from django.contrib.auth.models import Group
        public_groups = Group.objects.filter(name='Share with Public')
        if len(public_groups) != 1:
            public_group = False
        else:
            public_group = public_groups[0]


        shared_layers = []
        shared_layer_ids = []

        try:
            max_theme_id = TOCTheme.objects.latest('pk').pk + 1000
        except:
            max_theme_id = 1000
            pass
        # Add "Imported" Theme and Layers
        if request.user.is_authenticated():
            # get "Imported" Layers
            import_layers = ImportLayer.objects.filter(user=request.user)
            uploaded_layer_ids = []
            uploaded_layers = []
            for layer in import_layers:
                layer_dict = layer.toDict()
                # Add "Imported" Layers to {'layers': [...],}
                uploaded_layers.append(layer_dict)
                uploaded_layer_ids.append(layer_dict['id'])
            # create "Imported" Theme
            uploaded_theme_dict = {
                'layers': uploaded_layer_ids,
                'is_toc_theme': True,
                'display_name': "Imported",
                'id': max_theme_id,
                'description': 'User uploaded layers.'
            }

            # Add "Shared" Layers
            for shared_layer in ImportLayer.objects.shared_with_user(request.user).exclude(user=request.user):
                shared_layer_dict = shared_layer.toDict()
                shared_layers.append(shared_layer_dict)
                shared_layer_ids.append(shared_layer_dict['id'])
        else:
            # Add "Shared" Layers
            if public_group:
                for shared_layer in ImportLayer.objects.all():
                    if public_group in shared_layer.sharing_groups.all():
                        shared_layer_dict = shared_layer.toDict()
                        shared_layers.append(shared_layer_dict)
                        shared_layer_ids.append(shared_layer_dict['id'])

        # Add "Shared" Theme
        if len(shared_layer_ids) > 0:
            shared_theme_dict = {
                'layers': shared_layer_ids,
                'is_toc_theme': True,
                'display_name': "Shared",
                'id': max_theme_id+1,
                'description': 'Shared user uploaded layers.'
            }
        else:
            shared_theme_dict = False

        toc_list = []

        for toc in activeSettings.table_of_contents.all().order_by('order'):
            layer_list = []
            for themeOrdering in TOCThemeOrder.objects.filter(toc=toc).order_by('order'):
                theme = themeOrdering.theme
                for layer in theme.layers.all().order_by('name'):
                    layer_list.append(layer.toDict)


            theme_list = [themeOrder.theme.toDict for themeOrder in TOCThemeOrder.objects.filter(toc=toc).order_by('order')]
            if request.user.is_authenticated():
                    layer_list = layer_list + uploaded_layers
                    theme_list.append(uploaded_theme_dict)
            if shared_theme_dict:
                    layer_list = layer_list + shared_layers
                    theme_list.append(shared_theme_dict)
            toc_list.append({
                "tocid": toc.id,
                "name": toc.name,
                "order": toc.order,
                "layers": layer_list,
                "themes": theme_list
            })
        json = {
            "state": { "activeLayers": [] },
            "tocs": toc_list,
            "success": True
        }
        return HttpResponse(simplejson.dumps(json))
    except Exception as e:
        print("========= %s ==========" % str(e))
        pass
    json = {
        "state": { "activeLayers": [] },
        "layers": [layer.toDict for layer in Layer.objects.filter(is_sublayer=False).exclude(layer_type='placeholder').order_by('name')],
        "themes": [theme.toDict for theme in Theme.objects.all().order_by('display_name')],
        "success": True
    }
    return HttpResponse(simplejson.dumps(json))


def create_layer(request):
    if request.POST:
        try:
            url, name, type, themes = get_layer_components(request.POST)
            layer = Layer(
                url = url,
                name = name,
                layer_type = type
            )
            layer.save()

            for theme_id in themes:
                theme = Theme.objects.get(id=theme_id)
                layer.themes.add(theme)
            layer.save()

        except Exception, e:
            return HttpResponse(e.message, status=500)

        result = layer_result(layer, message="Saved Successfully")
        return HttpResponse(simplejson.dumps(result))


def update_layer(request, layer_id):
    if request.POST:
        layer = get_object_or_404(Layer, id=layer_id)

        try:
            url, name, type, themes = get_layer_components(request.POST)
            layer.url = url
            layer.name = name
            layer.save()

            for theme in layer.themes.all():
                layer.themes.remove(theme)
            for theme_id in themes:
                theme = Theme.objects.get(id=theme_id)
                layer.themes.add(theme)
            layer.save()

        except Exception, e:
            return HttpResponse(e.message, status=500)

        result = layer_result(layer, message="Edited Successfully")
        return HttpResponse(simplejson.dumps(result))


def get_layer_components(request_dict, url='', name='', type='XYZ', themes=[]):
    if 'url' in request_dict:
        url = request_dict['url']
    if 'name' in request_dict:
        name = request_dict['name']
    if 'type' in request_dict:
        type = request_dict['type']
    if 'themes' in request_dict:
        themes = request_dict.getlist('themes')
    return url, name, type, themes


def layer_result(layer, status_code=1, success=True, message="Success"):
    result = {
        "status_code":status_code,
        "success":success,
        "message":message,
        "layer": layer.toDict,
        "themes": [theme.id for theme in layer.themes.all()]
    }
    return result

def load_config(request):
    import json
    import os
    from django.core.exceptions import ObjectDoesNotExist
    from django.template.defaultfilters import slugify

    json_data = open('data_manager/fixtures/wa_config.json')
    wa_config = json.load(json_data)
    toc_obj = wa_config['Themes'][0]['Marine Spatial Planning']['TOC'][0]
    layers = wa_config['layersNew']
    base_url = wa_config['DNRAGSServiceURL']

    try:
        toc = TOC.objects.get(name='WA_CMSP')
    except ObjectDoesNotExist:
        toc = TOC(name='WA_CMSP')
        toc.save()
    for layer_name, layer_obj in layers.iteritems():
        if 'url' in layer_obj and layer_obj['url'] != "":
            relative_url = layer_obj['url'].replace('DNRAGSServiceURL/','')
            absolute_url = os.path.join(base_url, relative_url, 'export')
            try:
                layer = Layer.objects.get(name=layer_name)
            except ObjectDoesNotExist:
                layer = Layer(name=layer_name, layer_type='ArcRest', url=absolute_url, arcgis_layers='0')
                layer.save()

    for theme_name, layer_list in toc_obj.iteritems():
        try:
            theme = TOCTheme.objects.get(display_name=theme_name)
        except ObjectDoesNotExist:
            theme = TOCTheme(display_name=theme_name, name=slugify(theme_name))
            theme.save()
        for layer_obj in layer_list:
            try:
                layer = Layer.objects.get(name=layer_obj['layerID'])
                theme.layers.add(layer)
            except ObjectDoesNotExist:
                pass
        theme.save()
        toc.themes.add(theme)
    return HttpResponse('layers and themes successfully loaded into WA_CMSP TOC object', status=200)

def import_layer(request):
    import os, shutil
    from datetime import datetime
    from django.conf import settings
    from drawing.views import is_3857
    if request.method == 'POST':
        if len(request.FILES) > 0:
            files = []
            for key in request.FILES.keys():
                #at this point, file uploads only occur in one place, we don't care what they're named
                for post_file in request.FILES.getlist(key):
                    files.append(post_file)
            for f in files:
                filename = '%s_%s.zip' % (str(request.user.pk), key)
                import_file = os.path.join(settings.ZIPFILE_DIR, filename)
                with open(import_file, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                # validate file
                #  is it a zip?
                import zipfile
                try:
                    zip_ref = zipfile.ZipFile(import_file, 'r')
                except Exception as e:
                    os.remove(import_file)
                    json_response = {
                        "message": 'Uploaded file is not recognizable as a zipfile.',
                        "success": False
                    }
                    return HttpResponse(simplejson.dumps(json_response))
                # does it have the correct pieces?
                required_exts = ['dbf','shp', 'cpg', 'prj', 'shx']
                namelist = zip_ref.namelist()
                for ext in required_exts:
                    # if not any(ext in x for x in namelist):
                    ext_count = len([x for x in namelist if x.lower().endswith(ext)])
                    if not ext_count == 1:
                        json_response = {
                            "success": False
                        }
                        if ext_count > 1:
                            json_response['message'] = "Zipfile contains more than one file of filetype: %s" % ext
                        if ext_count < 1:
                            json_response['message'] = "No %s file in zipped file. Required filetypes: .cpg, .dbf, .prj, .shp, .shx" % ext
                        return HttpResponse(simplejson.dumps(json_response))
                shapefile_shp = [x for x in namelist if ".shp" in x.lower()][0]

                # unzip it
                unzip_dir_name = '%s_%s' % (str(request.user.pk), key)
                unzip_dir = os.path.join(settings.UPLOAD_DIR, unzip_dir_name)
                if os.path.exists(unzip_dir):
                    if os.path.isdir(unzip_dir):
                        try:
                            shutil.rmtree(unzip_dir, ignore_errors=True)
                        except Exception as e:
                            print("======== %s =========" % str(e))
                            pass
                    else:
                        os.remove(unzip_dir)

                try:
                    os.mkdir(unzip_dir)
                except Exception as e:
                    print("======== %s =========" % str(e))
                    pass

                try:
                    zip_ref.extractall(unzip_dir)
                except OSError as e:
                    print("======== %s =========" % str(e))
                    try:
                        zip_ref.close()
                        shutil.rmtree(unzip_dir, ignore_errors=True)
                    except:
                        pass
                    json_response = {
                        "message": "Error Unzipping file",
                        "success": False
                    }
                    return HttpResponse(simplejson.dumps(json_response))

                zip_ref.close()

                # remove obsolete zip file
                os.remove(import_file)

                # open shapefile
                from osgeo import ogr
                driver = ogr.GetDriverByName('ESRI Shapefile')
                try:
                    dataset = driver.Open(os.path.join(unzip_dir, shapefile_shp))
                    layer = dataset.GetLayer()
                    spatialRef = layer.GetSpatialRef()
                except Exception as e:
                    print("======== %s =========" % str(e))
                    import ipdb; ipdb.set_trace()
                    shutil.rmtree(unzip_dir, ignore_errors=True)
                    json_response = {
                        "message": str(e),
                        "success": False
                    }
                    return HttpResponse(simplejson.dumps(json_response))


                # is it in the correct projection?
                if not is_3857(spatialRef):
                    shutil.rmtree(unzip_dir, ignore_errors=True)
                    json_response = {
                        "message": "Imported shapefile is not projected as EPSG:3857 or as ArcGIS:'WGS 1984 Web Mercator (Auxiliary Sphere)'",
                        "success": False
                    }
                    return HttpResponse(simplejson.dumps(json_response))

                from data_manager.models import ImportLayer, ImportFeature
                now = datetime.now()

                # create Layer Object
                if 'name' in request.POST.keys():
                    layer_name = request.POST['name']
                else:
                    layer_name = 'Imported Layer %s' % now.strftime("%h %m, %Y")
                if 'description' in request.POST.keys():
                    layer_description = request.POST['description']
                else:
                    layer_description = "Imported %s" % now.strftime("%-I:%M %p on %h %m, %Y")
                try:
                    import_layer = ImportLayer.objects.create(user=request.user, description=layer_description, name=layer_name)
                except:
                    shutil.rmtree(unzip_dir, ignore_errors=True)
                    json_response = {
                        "message": "Unknown error: unable to create imported layer.",
                        "success": False
                    }
                    return HttpResponse(simplejson.dumps(json_response))

                from django.contrib.gis.geos import GEOSGeometry
                # Create Feature Object
                for geom in layer:
                    feature = simplejson.loads(geom.ExportToJson())['geometry']
                    geos_geom = GEOSGeometry(simplejson.dumps(feature))
                    # Store attributes (as a JSON blob for now)
                    feature_attributes = {}
                    for key in geom.keys():
                        feature_attributes[key] = geom[key]
                    feature_attribute_blob = simplejson.dumps(feature_attributes)
                    try:
                        feat = ImportFeature.objects.create(
                            # name=geom[settings.UPLOAD_NAME_ATTR],
                            geometry_orig=geos_geom,
                            geometry_final=geos_geom,
                            user_id=request.user.id,
                            summary=feature_attribute_blob
                        )
                        # associate feature with layer
                        feat.add_to_collection(import_layer)
                    except Exception as e:
                        print("======== %s =========" % str(e))
                        try:
                            shutil.rmtree(unzip_dir, ignore_errors=True)
                            #TODO: get all features belonging to import_layer and delete them!
                            # import ipdb; ipdb.set_trace()
                            import_layer.full_clean() # ??? maybe this does it?
                            import_layer.delete()
                        except Exception as e2:
                            print("======== %s =========" % str(e2))
                            pass
                        json_response = {
                            "message": "Unknown error: %s" % e,
                            "success": False
                        }
                        return HttpResponse(simplejson.dumps(json_response))

                shutil.rmtree(unzip_dir, ignore_errors=True)
            json_response = {
                "message": "Layer created",
                "success": True
            }
        else: # No files
            json_response = {
                "message": "No file uploaded",
                "success": False
            }
    else: # not POST
        json_response = {
            "message": "Invalid request method: Only POST accepted",
            "success": False
            # "status": 405
        }
    return HttpResponse(simplejson.dumps(json_response))

@cache_page(60 * 60 * 24, key_prefix="data_manager_import_layer_json")
def get_import_layer_json(request, uid):
    from madrona.features import get_feature_by_uid
    import_layer = get_feature_by_uid(uid)
    return HttpResponse(import_layer.geojson())

def delete_import_layer(request, layer_id):
    if request.user.is_authenticated():
        try:
            importLayer = ImportLayer.objects.get(pk=layer_id)
            importLayer.delete()
        except Exception as e:
            json_response = {
                "message": "No layer matching given ID",
                "success": False,
                "status": 400
            }
            return HttpResponse(simplejson.dumps(json_response))
        json_response = {
            "message": "Layer deleted.",
            "success": True,
            "status": 200
        }
        return HttpResponse(simplejson.dumps(json_response))
    else:
        json_response = {
            "message": "Not authorized.",
            "success": False,
            "status": 401
        }
        return HttpResponse(simplejson.dumps(json_response))

'''
'''
def share_import_layer(request):
    from django.contrib.auth.models import Group
    from madrona.features import get_feature_by_uid
    group_names = request.POST.getlist('groups[]')
    layer_uid = request.POST['import-layer']
    layer = get_feature_by_uid(layer_uid)
    viewable, response = layer.is_viewable(request.user)
    if not viewable:
        return response
    #remove previously shared with groups, before sharing with new list
    layer.share_with(None)
    groups = []
    for group_name in group_names:
        groups.append(Group.objects.get(name=group_name))
    layer.share_with(groups, append=False)
    return HttpResponse("", status=200)
