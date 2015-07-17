from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.views.decorators.cache import cache_page
from madrona.features.models import Feature
from madrona.features import get_feature_by_uid
from general.utils import meters_to_feet
from models import *
from simplejson import dumps
from django.contrib.gis.db.models.aggregates import Union


'''
'''
def sdc_analysis(request, sdc_id):
    from sdc_analysis import display_sdc_analysis
    sdc_obj = get_object_or_404(Scenario, pk=sdc_id)
    #check permissions
    viewable, response = sdc_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_sdc_analysis(request, sdc_obj)

'''
'''
def copy_design(request, uid):
    try:
        design_obj = get_feature_by_uid(uid)
    except Feature.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = design_obj.is_viewable(request.user)
    if not viewable:
        return response

    design_obj.pk = None
    design_obj.user = request.user
    design_obj.save()

    json = []
    json.append({
        'id': design_obj.id,
        'uid': design_obj.uid,
        'name': design_obj.name,
        'description': design_obj.description,
        'attributes': design_obj.serialize_attributes
    })

    return HttpResponse(dumps(json), status=200)

'''
'''
def delete_design(request, uid):
    try:
        design_obj = get_feature_by_uid(uid)
    except Feature.DoesNotExist:
        raise Http404

    #check permissions
    viewable, response = design_obj.is_viewable(request.user)
    if not viewable:
        return response

    design_obj.delete()
    #design_obj.active = False
    #design_obj.save(rerun=False)

    return HttpResponse("", status=200)

'''
'''
def get_scenarios(request):
    json = []

    scenarios = Scenario.objects.filter(user=request.user, active=True).order_by('date_created')
    for scenario in scenarios:
        sharing_groups = [group.name for group in scenario.sharing_groups.all()]
        json.append({
            'id': scenario.id,
            'uid': scenario.uid,
            'name': scenario.name,
            'description': scenario.description,
            'attributes': scenario.serialize_attributes,
            'sharing_groups': sharing_groups
        })

    shared_scenarios = Scenario.objects.shared_with_user(request.user)
    for scenario in shared_scenarios:
        if scenario.active and scenario not in scenarios:
            username = scenario.user.username
            actual_name = scenario.user.first_name + ' ' + scenario.user.last_name
            json.append({
                'id': scenario.id,
                'uid': scenario.uid,
                'name': scenario.name,
                'description': scenario.description,
                'attributes': scenario.serialize_attributes,
                'shared': True,
                'shared_by_username': username,
                'shared_by_name': actual_name
            })

    return HttpResponse(dumps(json))

'''
'''
def get_selections(request):
    json = []
    selections = LeaseBlockSelection.objects.filter(user=request.user).order_by('date_created')
    for selection in selections:
        sharing_groups = [group.name for group in selection.sharing_groups.all()]
        json.append({
            'id': selection.id,
            'uid': selection.uid,
            'name': selection.name,
            'description': selection.description,
            'attributes': selection.serialize_attributes,
            'sharing_groups': sharing_groups
        })

    shared_selections = LeaseBlockSelection.objects.shared_with_user(request.user)
    for selection in shared_selections:
        if selection not in selections:
            username = selection.user.username
            actual_name = selection.user.first_name + ' ' + selection.user.last_name
            json.append({
                'id': selection.id,
                'uid': selection.uid,
                'name': selection.name,
                'description': selection.description,
                'attributes': selection.serialize_attributes,
                'shared': True,
                'shared_by_username': username,
                'shared_by_name': actual_name
            })

    return HttpResponse(dumps(json))

'''
'''
def get_leaseblock_features(request):
    from madrona.common.jsonutils import get_properties_json, get_feature_json, srid_to_urn, srid_to_proj
    srid = settings.GEOJSON_SRID
    leaseblock_ids = request.GET.getlist('leaseblock_ids[]')
    leaseblocks = LeaseBlock.objects.filter(prot_numb__in=leaseblock_ids)
    feature_jsons = []
    for leaseblock in leaseblocks:
        try:
            geom = leaseblock.geometry.transform(srid, clone=True).json
        except:
            srid = settings.GEOJSON_SRID_BACKUP
            geom = leaseblock.geometry.transform(srid, clone=True).json
        feature_jsons.append(get_feature_json(geom, json.dumps('')))#json.dumps(props)))
        #feature_jsons.append(leaseblock.geometry.transform(srid, clone=True).json)
        '''
        geojson = """{
          "type": "Feature",
          "geometry": %s,
          "properties": {}
        }""" %leaseblock.geometry.transform(settings.GEOJSON_SRID, clone=True).json
        '''
        #json.append({'type': "Feature", 'geometry': leaseblock.geometry.geojson, 'properties': {}})
    #return HttpResponse(dumps(json[0]))
    geojson = """{
      "type": "FeatureCollection",
      "crs": { "type": "name", "properties": {"name": "%s"}},
      "features": [
      %s
      ]
    }""" % (srid_to_urn(srid), ', \n'.join(feature_jsons),)
    return HttpResponse(geojson)

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

    return HttpResponse(dumps(scenario_obj.serialize_attributes))

'''
'''
def get_sharing_groups(request):
    from madrona.features import user_sharing_groups
    from functools import cmp_to_key
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    json = []
    sharing_groups = user_sharing_groups(request.user)
    for group in sharing_groups:
        members = []
        for user in group.user_set.all():
            if user.first_name.replace(' ', '') != '' and user.last_name.replace(' ', '') != '':
                members.append(user.first_name + ' ' + user.last_name)
            else:
                members.append(user.username)
        sorted_members = sorted(members, key=cmp_to_key(locale.strcoll))
        json.append({
            'group_name': group.name,
            'group_slug': slugify(group.name)+'-sharing',
            'members': sorted_members
        })
    return HttpResponse(dumps(json))

'''
'''
def share_design(request):
    from django.contrib.auth.models import Group
    group_names = request.POST.getlist('groups[]')
    design_uid = request.POST['scenario']
    design = get_feature_by_uid(design_uid)
    viewable, response = design.is_viewable(request.user)
    if not viewable:
        return response
    #remove previously shared with groups, before sharing with new list
    design.share_with(None)
    groups = []
    for group_name in group_names:
        groups.append(Group.objects.get(name=group_name))
    design.share_with(groups, append=False)
    return HttpResponse("", status=200)

'''
'''


def run_filter_query(filters):
    from collections import OrderedDict
    import ast
    # TODO: This would be nicer if it generically knew how to filter fields
    # by name, and what kinds of filters they were. For now, hard code.
    notes = []
    query = GridCell.objects.all()

    if 'species' in filters.keys() and filters['species']:
        spcs_occ = SpeciesHabitatOccurence.objects.filter(species_common=filters['species_input'])
        if 'lifestage' in filters.keys() and filters['lifestage']:
            spcs_occ = spcs_occ.filter(lifestage=filters['lifestage_input'])
        lu_codes = [x.sgh_lookup_code for x in spcs_occ]
        lu_codes = OrderedDict.fromkeys(lu_codes).keys()
        pmin = False
        pmax = False
        amin = False
        amax = False
        for spcs in spcs_occ:
            if (spcs.preferred_min_depth >= 0) and (not pmin or pmin > spcs.preferred_min_depth):
                pmin = spcs.preferred_min_depth
            if (spcs.preferred_max_depth >= 0) and (not pmax or pmax < spcs.preferred_max_depth):
                pmax = spcs.preferred_max_depth
            if (spcs.absolute_min_depth >= 0) and (not amin or amin > spcs.absolute_min_depth):
                amin = spcs.absolute_min_depth
            if (spcs.absolute_max_depth >= 0) and (not amax or amax < spcs.absolute_max_depth):
                amax = spcs.absolute_max_depth

        lookup_qs = PlanningUnitHabitatLookup.objects.filter(sgh_lookup_code__in=lu_codes)

        pug_ids = [pug_id for id_list in lookup_qs for pug_id in ast.literal_eval(id_list.pug_ids)]
        query = query.filter(unique_id__in=pug_ids)
        if pmin and pmax:
            query = query.filter(max_meter__gte=pmin)
            query = query.filter(min_meter__lte=pmax)
        elif amin and amax:
            notes.append('No known preferred depths, using absolute depths')
            query = query.filter(max_meter__gte=amin)
            query = query.filter(min_meter__lte=amax)
        else:
            notes.append('No known preferred or absolute depths, using all depths')

    if 'mean_fthm' in filters.keys() and filters['mean_fthm']:
        # query = query.filter(depth_mean__range=(filters['depth_min'], filters['depth_max']))
        query = query.filter(mean_fthm__gte=filters['mean_fthm_min'])
        query = query.filter(mean_fthm__lte=filters['mean_fthm_max'])

    if 'cnt_cs' in filters.keys() and filters['cnt_cs']:
        if filters['cnt_cs_input'] == 'Y':
            query = query.filter(cnt_cs__gt=0)
        else:
            query = query.exclude(cnt_cs__gt=0)

    if 'cnt_penn' in filters.keys() and filters['cnt_penn']:
        if filters['cnt_penn_input'] == 'Y':
            query = query.filter(cnt_penn__gt=0)
        else:
            query = query.exclude(cnt_penn__gt=0)

    if 'sft_sub_m2' in filters.keys() and filters['sft_sub_m2']:
        if filters['sft_sub_m2_input'] == 'Y':
            query = query.filter(sft_sub_m2__gt=0)
        else:
            query = query.exclude(sft_sub_m2__gt=0)

    if 'mix_sub_m2' in filters.keys() and filters['mix_sub_m2']:
        if filters['mix_sub_m2_input'] == 'Y':
            query = query.filter(mix_sub_m2__gt=0)
        else:
            query = query.exclude(mix_sub_m2__gt=0)

    if 'hrd_sub_m2' in filters.keys() and filters['hrd_sub_m2']:
        if filters['hrd_sub_m2_input'] == 'Y':
            query = query.filter(hrd_sub_m2__gt=0)
        else:
            query = query.exclude(hrd_sub_m2__gt=0)

    if 'rck_sub_m2' in filters.keys() and filters['rck_sub_m2']:
        if filters['rck_sub_m2_input'] == 'Y':
            query = query.filter(rck_sub_m2__gt=0)
        else:
            query = query.exclude(rck_sub_m2__gt=0)

    if 'hsall_m2' in filters.keys() and 'hsall_m2_checkboxes' in filters.keys():

        if type(filters['hsall_m2_checkboxes']) is list:
            # save and filter submissions are handled differently since
            # not all of these fields exist on the model.
            # This step maps out the model data during a save to work like filtering.
            if '1' in filters['hsall_m2_checkboxes'] and 'hsall_m2_checkboxes_1' not in filters.keys():
                filters['hsall_m2_checkboxes_1'] = 'true';
            if '2' in filters['hsall_m2_checkboxes'] and 'hsall_m2_checkboxes_2' not in filters.keys():
                filters['hsall_m2_checkboxes_2'] = 'true';
            if '3' in filters['hsall_m2_checkboxes'] and 'hsall_m2_checkboxes_3' not in filters.keys():
                filters['hsall_m2_checkboxes_3'] = 'true';
            if '4' in filters['hsall_m2_checkboxes'] and 'hsall_m2_checkboxes_4' not in filters.keys():
                filters['hsall_m2_checkboxes_4'] = 'true';

        from django.db.models import Q
        if "hsall_m2_checkboxes_1" in filters.keys():
            if "hsall_m2_checkboxes_2" in filters.keys():
                if "hsall_m2_checkboxes_3" in filters.keys():
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall2_m2__gt=0) | Q(hsall3_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall2_m2__gt=0) | Q(hsall3_m2__gt=0))
                else:
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall2_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall2_m2__gt=0))
            else:
                if "hsall_m2_checkboxes_3" in filters.keys():
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall3_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall3_m2__gt=0))
                else:
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall1_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(hsall1_m2__gt=0)
        else:
            if "hsall_m2_checkboxes_2" in filters.keys():
                if "hsall_m2_checkboxes_3" in filters.keys():
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall2_m2__gt=0) | Q(hsall3_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(Q(hsall2_m2__gt=0) | Q(hsall3_m2__gt=0))
                else:
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall2_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(hsall2_m2__gt=0)
            else:
                if "hsall_m2_checkboxes_3" in filters.keys():
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(Q(hsall3_m2__gt=0) | Q(hsall4_m2__gt=0))
                    else:
                        query = query.filter(hsall3_m2__gt=0)
                else:
                    if "hsall_m2_checkboxes_4" in filters.keys():
                        query = query.filter(hsall4_m2__gt=0)

    # if 'hsall1_m2' in filters.keys() and filters['hsall1_m2']:
    #     hsall1_m2 = float(filters['hsall1_m2_min']) * 1000000.0
    #     query = query.filter(hsall1_m2__gte=hsall1_m2)

    # if 'hsall2_m2' in filters.keys() and filters['hsall2_m2']:
    #     hsall2_m2 = float(filters['hsall2_m2_min']) * 1000000.0
    #     query = query.filter(hsall2_m2__gte=hsall2_m2)

    # if 'hsall3_m2' in filters.keys() and filters['hsall3_m2']:
    #     hsall3_m2 = float(filters['hsall3_m2_min']) * 1000000.0
    #     query = query.filter(hsall3_m2__gte=hsall3_m2)

    # if 'hsall4_m2' in filters.keys() and filters['hsall4_m2']:
    #     hsall4_m2 = float(filters['hsall4_m2_min']) * 1000000.0
    #     query = query.filter(hsall4_m2__gte=hsall4_m2)

    if 'hpc_est_m2' in filters.keys() and filters['hpc_est_m2']:
        hpc_est_m2 = float(filters['hpc_est_m2_min']) * 1000000.0
        query = query.filter(hpc_est_m2__gte=hpc_est_m2)

    if 'hpc_klp_m2' in filters.keys() and filters['hpc_klp_m2']:
        hpc_klp_m2 = float(filters['hpc_klp_m2_min']) * 1000000.0
        query = query.filter(hpc_klp_m2__gte=hpc_klp_m2)

    if 'hpc_rck_m2' in filters.keys() and filters['hpc_rck_m2']:
        hpc_rck_m2 = float(filters['hpc_rck_m2_min']) * 1000000.0
        query = query.filter(hpc_rck_m2__gte=hpc_rck_m2)

    if 'hpc_sgr_m2' in filters.keys() and filters['hpc_sgr_m2']:
        hpc_sgr_m2 = float(filters['hpc_sgr_m2_min']) * 1000000.0
        query = query.filter(hpc_sgr_m2__gte=hpc_sgr_m2)

    return (query, notes)

'''
'''
@cache_page(60 * 60) # 1 hour of caching
def get_filter_count(request):
    filter_dict = dict(request.GET.iteritems())
    (query, notes) = run_filter_query(filter_dict)
    return HttpResponse(query.count(), status=200)


'''
'''
@cache_page(60 * 60) # 1 hour of caching
def get_filter_results(request):
    filter_dict = dict(request.GET.iteritems())

    (query, notes) = run_filter_query(filter_dict)

    json = []
    count = query.count()
    if count == 0:
        json = [{
            'count': 0,
            'wkt': None
        }]
    else:
        dissolved_geom = query.aggregate(Union('geometry'))
        if dissolved_geom['geometry__union']:
            dissolved_geom = dissolved_geom['geometry__union']
        else:
            raise Exception("No lease blocks available with the current filters.")
        json = [{
            'count': count,
            'wkt': dissolved_geom.wkt
        }]
        # if type(dissolved_geom) == MultiPolygon:
        #     self.geometry_dissolved = dissolved_geom
        # else:
        #     self.geometry_dissolved = MultiPolygon(dissolved_geom, srid=dissolved_geom.srid)

    # return # of grid cells and dissolved geometry in geojson
    return HttpResponse(dumps(json))

'''
'''
#@cache_page(60 * 60 * 24, key_prefix="scenarios_get_leaseblocks")
def get_leaseblocks(request):
    json = []
    for grid_cell in GridCell.objects.all():
        json.append({
            'id': grid_cell.id,
            'shore_distance': grid_cell.shore_distance,
            'pier_distance': grid_cell.pier_distance,
            'inlet_distance': grid_cell.inlet_distance,
            'outfall_distance': grid_cell.outfall_distance,
            'fish_richness': grid_cell.fish_richness,
            'coral_richness': grid_cell.coral_richness,
            'coral_density': grid_cell.coral_density,
            'coral_size': grid_cell.coral_size
        })
    return HttpResponse(dumps(json))
