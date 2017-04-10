from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.gis.geos import GEOSGeometry
from madrona.features.models import Feature
from madrona.features import get_feature_by_uid
from madrona.common.utils import LargestPolyFromMulti
from scenarios.models import GridCell, Scenario
from models import *
from ofr_manipulators import clip_to_grid
from simplejson import dumps



'''
'''
def get_drawings(request):
    json = []

    public_group = get_public_group()

    if request.user.is_authenticated():
        drawings = AOI.objects.filter(user=request.user).order_by('date_created')

        for drawing in drawings:
            sharing_groups = [group.name for group in drawing.sharing_groups.all()]
            display_name = "[%s] %s" % (drawing.collection.name, drawing.name) if drawing.collection else drawing.name
            json.append({
                'id': drawing.id,
                'uid': drawing.uid,
                'name': drawing.name,
                'display_name': display_name,
                'description': drawing.description,
                'attributes': drawing.serialize_attributes,
                'sharing_groups': sharing_groups
            })

        shared_drawings = AOI.objects.shared_with_user(request.user)
        for drawing in shared_drawings:
            if drawing not in drawings:
                username = drawing.user.username
                actual_name = drawing.user.first_name + ' ' + drawing.user.last_name
                public = public_group in drawing.sharing_groups.all()
                display_name = "[%s] %s" % (drawing.collection.name, drawing.name) if drawing.collection else drawing.name
                json.append({
                    'id': drawing.id,
                    'uid': drawing.uid,
                    'name': drawing.name,
                    'display_name': display_name,
                    'description': drawing.description,
                    'attributes': drawing.serialize_attributes,
                    'shared': True,
                    'shared_by_username': username,
                    'shared_by_name': actual_name,
                    'public': public
                })

        groups = list(request.user.groups.all())
        if public_group and not public_group in request.user.groups.all():
            groups = groups + [public_group]
        shared_drawings_list = list(shared_drawings)
    else:
        if public_group:
            groups = [public_group]
        else:
            groups = []
        drawings = []
        shared_drawings_list = []

    for group in groups:
        group_shared_drawings = AOI.objects.filter(sharing_groups=group)
        for drawing in group_shared_drawings:
            if drawing not in drawings and drawing not in shared_drawings_list:
                shared_drawings_list.append(drawing)
                username = drawing.user.username
                actual_name = drawing.user.first_name + ' ' + drawing.user.last_name
                public = public_group in drawing.sharing_groups.all()
                json.append({
                    'id': drawing.id,
                    'uid': drawing.uid,
                    'name': drawing.name,
                    'description': drawing.description,
                    'attributes': drawing.serialize_attributes,
                    'shared': True,
                    'shared_by_username': username,
                    'shared_by_name': actual_name,
                    'public': public
                })

    return HttpResponse(dumps(json))

'''
'''
def delete_drawing(request, uid):
    try:
        drawing_obj = get_feature_by_uid(uid)
    except Feature.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = drawing_obj.is_viewable(request.user)
    if not viewable:
        return response

    drawing_obj.delete()

    return HttpResponse("", status=200)

'''
'''
def get_clipped_shape(request):
    zero = .01

    if not (request.POST and request.POST['target_shape']):
        return HTTPResponse("No shape submitted", status=400)

    target_shape = request.POST['target_shape']
    geom = GEOSGeometry(target_shape, srid=3857)

    clipped_shape = clip_to_grid(geom)

    # return new_shape['geometry__union']
    if clipped_shape and clipped_shape.area >= zero: #there was overlap
        largest_poly = LargestPolyFromMulti(clipped_shape)
        wkt = largest_poly.wkt
        return HttpResponse(dumps({"clipped_wkt": wkt}), status=200)
    else:
        return HttpResponse("Submitted Shape is outside Grid Cell Boundaries (no overlap).", status=400)

    # return HttpResponse(dumps({"clipped_wkt": wkt}), status=200)

'''
'''
def aoi_analysis(request, aoi_id):
    from aoi_analysis import display_aoi_analysis
    aoi_obj = get_object_or_404(AOI, pk=aoi_id)
    #check permissions
    viewable, response = aoi_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_aoi_analysis(request, aoi_obj)
    # Create your views here.

'''
'''
def get_attributes(request, uid):
    try:
        scenario_obj = get_feature_by_uid(uid)
    except Scenario.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = scenario_obj.is_viewable(request.user)
    if not viewable:
        return response

    if 'serialize_attributes' in dir(scenario_obj):
        if hasattr(scenario_obj,'is_loading') and scenario_obj.is_loading:
            scenario_obj.save()
        return HttpResponse(dumps(scenario_obj.serialize_attributes))
    else:
        return HttpResponse(dumps([]))

'''
'''
def get_geometry_orig(request, uid):
    try:
        scenario_obj = get_feature_by_uid(uid)
        wkt = scenario_obj.geometry_orig.wkt
    except Scenario.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = scenario_obj.is_viewable(request.user)
    if not viewable:
        return response

    return HttpResponse(dumps({"geometry_orig": wkt}), status=200)


def copy_collection(request, uid):
    try:
        original_collection = get_feature_by_uid(uid)
        copy_name = "(Copy) %s" % original_collection.name
        copy_description = "Copy of %s" % original_collection.name
        copy = Collection.objects.create(user=request.user, name=copy_name, description=copy_description)
        from scenarios.views import copy_design
        for original_feature in original_collection.feature_set():
            copy_design(request, original_feature.uid, copy)
        return HttpResponse(dumps({'success':True, 'copy_id': copy.id, 'copy_uid': copy.uid}), status=200)
    except:
        return HttpResponse('Failed to create collection copy.', status=500)

'''
'''
def get_collections(request):
    json = []

    public_group = get_public_group()

    if request.user.is_authenticated():
        collections = Collection.objects.filter(user=request.user).order_by('date_created')

        for collection in collections:
            sharing_groups = [group.name for group in collection.sharing_groups.all()]
            json.append({
                'id': collection.id,
                'uid': collection.uid,
                'name': collection.name,
                'description': collection.description,
                'attributes': {'attributes':[{'Status': 'Loading...'}], 'event':''},
                'sharing_groups': sharing_groups
            })

        shared_collections = Collection.objects.shared_with_user(request.user)
        for collection in shared_collections:
            if collection not in collections:
                username = collection.user.username
                actual_name = collection.user.first_name + ' ' + collection.user.last_name
                public = public_group in collection.sharing_groups.all()
                json.append({
                    'id': collection.id,
                    'uid': collection.uid,
                    'name': collection.name,
                    'description': collection.description,
                    # 'attributes': collection.serialize_attributes,
                    'shared': True,
                    'shared_by_username': username,
                    'shared_by_name': actual_name,
                    'public': public
                })

        groups = list(request.user.groups.all())
        if public_group and not public_group in request.user.groups.all():
            groups = groups + [public_group]
        shared_collections_list = list(shared_collections)
    else:
        if public_group:
            groups = [public_group]
        else:
            groups = []
        collections = []
        shared_collections_list = []

    for group in groups:
        group_shared_collections = Collection.objects.filter(sharing_groups=group)
        for collection in group_shared_collections:
            if collection not in collections and collection not in shared_collections_list:
                shared_collections_list.append(drawing)
                username = collection.user.username
                actual_name = collection.user.first_name + ' ' + collection.user.last_name
                public = public_group in collection.sharing_groups.all()
                json.append({
                    'id': collection.id,
                    'uid': collection.uid,
                    'name': collection.name,
                    'description': collection.description,
                    # 'attributes': collection.serialize_attributes,
                    'shared': True,
                    'shared_by_username': username,
                    'shared_by_name': actual_name,
                    'public': public
                })

    return HttpResponse(dumps(json))

def get_collection_attributes(request, uid):
    if request.user.is_authenticated():
        try:
            collection = get_feature_by_uid(uid)
        except Exception as e:
            return HttpResponse("No collection of this uid: %s" % uid, status=404)
        (viewable, response) = collection.is_viewable(request.user)
        if viewable:
            json={'attributes':collection.serialize_attributes}
            return HttpResponse(dumps(json), status=200)
        return HttpResponse("User not authorized to view collection: %s" % uid, status=403)
    return HttpResponse("User not authenticated", status=401)



def delete_collection(request, uid):
    try:
        collection_obj = get_feature_by_uid(uid)
    except Feature.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = collection_obj.is_viewable(request.user)
    if not viewable:
        return response

    for associated_feature in collection_obj.feature_set():
        associated_feature.delete()
    # TODO: (frontend) "Are you sure?"
    collection_obj.delete()

    return HttpResponse("", status=200)

def get_public_group():
    public_groups = Group.objects.filter(name='Share with Public')
    if len(public_groups) != 1:
        public_group = False
    else:
        public_group = public_groups[0]

    return public_group

def form_resources(request, uid=None):
    from madrona.features.views import form_resources as madrona_form_resources
    from drawing.models import Collection
    if request.method == 'POST':
        if len(request.FILES) > 0:
            #TODO associate shapefile features with newly created scenario
            madrona_return = madrona_form_resources(request, Collection, uid)
            #TODO unpack uploaded files if present
            try:
                if madrona_return.status_code == 201:
                    collection = get_feature_by_uid(madrona_return.get('X-Madrona-Select'))
                    madrona_return = unpack_shapefile_upload(request, collection, madrona_return)
                    if not madrona_return.status_code == 201:
                        collection.delete()
            except Exception as e:
                pass
            return madrona_return

    return madrona_form_resources(request, Collection, uid)

def unpack_shapefile_upload(request, collection, retval):
    files = []
    for key in request.FILES.keys():
        #at this point, file uploads only occur in one place, we don't care what they're named
        for post_file in request.FILES.getlist(key):
            files.append(post_file)
    for f in files:
        with open(settings.ZIPFILE_PATH, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        import zipfile
        try:
            zip_ref = zipfile.ZipFile(settings.ZIPFILE_PATH, 'r')
        except Exception as e:
            return fail_upload_check(retval, "Uploaded file does not appear to be a zipfile")
        # check for required files
        required_exts = ['dbf','shp', 'cpg', 'prj', 'shx']
        namelist = zip_ref.namelist()
        for ext in required_exts:
            # if not any(ext in x for x in namelist):
            ext_count = len([x for x in namelist if x.lower().endswith(ext)])
            if ext_count > 1:
                return fail_upload_check(retval, "Zipfile contains more than one file of filetype: %s" % ext)
            if ext_count < 1:
                return fail_upload_check(retval, "Zipfile does not contain all required filetypes: .cpg, .dbf, .prj, .shp, .shx")
        shapefile_shp = [x for x in namelist if ".shp" in x.lower()][0]

        # unzip it
        zip_ref.extractall(settings.UPLOAD_DIR)
        zip_ref.close()

        # open shapefile
        from osgeo import ogr
        driver = ogr.GetDriverByName('ESRI Shapefile')
        dataset = driver.Open(r'%s/%s' % (settings.UPLOAD_DIR, shapefile_shp))
        layer = dataset.GetLayer()
        spatialRef = layer.GetSpatialRef()

        if not is_3857(spatialRef):
            error_message = "Imported shapefile is not projected as EPSG:3857 or as ArcGIS:'WGS 1984 Web Mercator (Auxiliary Sphere)'"
            return fail_upload_check(retval, error_message)

        # check for required fields
        upload_fields = [settings.UPLOAD_ACTION_ATTR, settings.UPLOAD_NAME_ATTR]
        geom = layer[0]
        if not (cmp(geom.keys().sort(),upload_fields.sort())==0):
            error_message = "Incorrect attribute names. Must match: %s" % str(upload_fields)
            return fail_upload_check(retval, error_message)

        #   * test if correct data types
        for field in upload_fields:
            fieldType = str
            if not type(geom[field]) == fieldType:
                error_message = "Field type mismatch: %s should be %s" % (field, fieldType)
                return fail_upload_check(retval, error_message)

        #6 convert to AOIs
        from django.contrib.gis.geos import GEOSGeometry
        import simplejson
        for geom in layer:
            feature = simplejson.loads(geom.ExportToJson())['geometry']
            geos_geom = GEOSGeometry(simplejson.dumps(feature))
            if settings.UPLOAD_ACTION_ATTR in geom.keys():
                reg_action=geom[settings.UPLOAD_ACTION_ATTR]
            else:
                reg_action='none'
            if settings.UPLOAD_DESCRIPTION_ATTR in geom.keys():
                description=geom[settings.UPLOAD_DESCRIPTION_ATTR]
            else:
                description=None

            try:
                aoi = AOI.objects.create(
                    name=geom[settings.UPLOAD_NAME_ATTR],
                    reg_action=reg_action,
                    description=description,
                    geometry_orig=geos_geom,
                    geometry_final=geos_geom,
                    user_id=request.user.id
                )
                aoi.add_to_collection(collection)
            except Exception as e:
                print("================%s=================" % e)
                pass
        #   6A polygon and multipolygon
        #7 associate AOIs with collection
    return retval

def fail_upload_check(retval, error_message):
    setattr(retval, 'status_code', 412)
    # setattr(retval, 'content', '{"status": 412, "message": "%s"}' % error_message)
    setattr(retval, 'content', error_message)
    print("========%s==========" % error_message)
    return retval

#   * test if EPSG:3857
def is_3857(spatialRef):
    from osgeo import osr
    #   TODO determine projection and handle a variety of projections
    #Innocent until proven guilty
    ret = True
    source_3857 = osr.SpatialReference()
    source_3857.ImportFromEPSG(3857)
    if spatialRef.IsSame(source_3857):
        return ret
    # arcgis_web_merc_wkt = 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["WGS_1984",SPHEROID["WGS_84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]'
    web_merc_wkt_tests = [
        '"WGS_1984_Web_Mercator_Auxiliary_Sphere"',
        '"GCS_WGS_1984"',
        'SPHEROID["WGS_84",63781',
        'PRIMEM["Greenwich",0',
        'UNIT["Degree",0.0174532925',
        'PROJECTION["Mercator_Auxiliary_Sphere"]',
        'PARAMETER["False_Easting",0.0]',
        'PARAMETER["False_Northing",0.0]',
        'PARAMETER["Central_Meridian",0.0]',
        'PARAMETER["Standard_Parallel_1",0.0]',
        'PARAMETER["Auxiliary_Sphere_Type",0.0]',
        'UNIT["Meter",1.0]'
    ]
    spatialRef_wkt = spatialRef.ExportToWkt()
    for test in web_merc_wkt_tests:
        if test not in spatialRef_wkt:
            print("============%s===============" % test)
            print(spatialRef_wkt)
            ret = False
    return ret
