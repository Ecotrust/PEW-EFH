from scenarios.models import GridCell as ScenarioGridCell
from django.contrib.gis.db.models.aggregates import Union

def clip_to_grid(geom, drawing=False):
    if drawing:
        intersection = intersecting_drawing_cells(geom)
    else:
        intersection = intersecting_cells(geom)

    new_shape = intersection.aggregate(Union('geometry'))
    if len(intersection) == 1:
        #single cells come back as a multipolygon
        clipped_shape = new_shape['geometry__union'].simplify();
    else:
        clipped_shape = new_shape['geometry__union'];

    return clipped_shape

def intersecting_cells(geom):
    intersection = ScenarioGridCell.objects.filter(centroid__intersects=geom)
    return intersection
    # if len(intersection) > 0:
	#        return intersection
    # else:
	#        return GridCell.objects.filter(geometry__intersects=geom)

def intersecting_drawing_cells(geom):
    from drawing.models import GridCell as DrawingGridCell
    intersection = DrawingGridCell.objects.filter(centroid__intersects=geom)
    return intersection
