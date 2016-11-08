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
        return HttpResponse(dumps(copy), status=200)
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
                # 'attributes': collection.serialize_attributes,
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
