from general.utils import format_precision
from decimal import Decimal


def get_min(grid_cells, field):
    min = getattr(grid_cells[0], field)
    for gc in grid_cells:
        if getattr(gc, field) < min:
            min = getattr(gc, field)
    return min


def get_max(grid_cells, field):
    max = getattr(grid_cells[0], field)
    for gc in grid_cells:
        if getattr(gc, field) > max:
            max = getattr(gc, field)
    return max


def get_range(grid_cells, field):
    min = getattr(grid_cells[0], field)
    max = getattr(grid_cells[0], field)
    for gc in grid_cells:
        if getattr(gc, field) < min:
            min = getattr(gc, field)
        if getattr(gc, field) > max:
            max = getattr(gc, field)
    return min, max


def get_value_count(grid_cells, field, value):
    count = 0
    for gc in grid_cells:
        if getattr(gc, field) == value:
            count += 1
    return count


def get_sum(grid_cells, field):
    sum_val = 0
    for gc in grid_cells:
        if getattr(gc, field):
            sum_val += getattr(gc, field)
    return sum_val


def get_average(grid_cells, field):
    cell_count = grid_cells.count()
    if cell_count == 0:
        return 0
    sum = get_sum(grid_cells, field)
    return sum / cell_count

def get_adjusted_average(grid_cells, field):
    cell_count = grid_cells.count()
    if cell_count == 0:
        return 0
    sum_val = Decimal(0)
    total_area = Decimal(0)
    for gc in grid_cells:
        try:
            cell_area = gc.geometry.area
            cell_val = getattr(gc, field)
            sum_val += Decimal(cell_val * Decimal(cell_area))
            total_area += Decimal(cell_area)
        except:
            # In case getattr fails
            pass
    return sum_val / total_area


def get_unique_values(grid_cells, field):
    values = []
    for gc in grid_cells:
        value = getattr(gc, field)
        if value not in values:
            values.append(value)
    return values


def format_area(value, raw):
    if raw:
        return str(float(value)) + ' sq mi'
    else:
        return str(format_precision(float(value), 0)) + ' sq mi'


def get_drawing_summary_reports(grid_cells, attributes, raw=False):
    from general.utils import sq_meters_to_sq_miles
    if grid_cells.count() == 0:
        attributes.append({'title': 'Total Area', 'data': '0 sq mi'})
        attributes.append({'title': 'Soft', 'data': '0 sq mi'})
        attributes.append({'title': 'Mixed', 'data': '0 sq mi'})
        attributes.append({'title': 'Hard', 'data': '0 sq mi'})
        attributes.append({'title': 'Inferred Rock', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 1 for all coral and sponges', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 2 for all coral and sponges', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 3 for all coral and sponges', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 4 for all coral and sponges', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 1 for Scleractinia coral', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 2 for Scleractinia coral', 'data': '0 sq mi'})
        attributes.append({'title': 'PHS 3 for Scleractinia coral', 'data': '0 sq mi'})
        return

    # # Number of Grid Cells
    # cell_count = grid_cells.count()
    # attributes.append({'title': 'Number of Grid Cells (drawing)', 'data': format(cell_count, ',d')})
    #

    # Total Area
    title = 'Total Area'
    area = sq_meters_to_sq_miles(sum([x.geometry.transform(2163, clone=True).area for x in grid_cells]))
    data = format_area(area, raw)
    attributes.append({'title': title, 'data': data})

    # Depth Range
    title = 'Depth Range'
    min_depth = get_min(grid_cells, 'depth')
    max_depth = get_max(grid_cells, 'depth')
    depth_range = '%s to %s fathoms' % (format_precision(float(min_depth), 0), format_precision(float(max_depth), 0))
    attributes.append({'title': title, 'data': depth_range})

    # Mean Depth
    title = 'Mean Depth'
    mean_depth = get_average(grid_cells, 'depth')
    data = str(format_precision(float(mean_depth), 0)) + ' fathoms'
    attributes.append({'title': title, 'data': data})

    # Soft Substrate (Area)
    title = 'Soft'
    soft_sub_area = get_sum(grid_cells, 'sft_sub_m2')
    data = format_area(soft_sub_area, raw)
    attributes.append({'title': title, 'data': data})

    # Mixed Substrate (Area)
    title = 'Mixed'
    mixed_sub_area = get_sum(grid_cells, 'mix_sub_m2')
    data = format_area(mixed_sub_area, raw)
    attributes.append({'title': title, 'data': data})

    # Hard Substrate (Area)
    title = 'Hard'
    hard_sub_area = get_sum(grid_cells, 'hrd_sub_m2')
    data = format_area(hard_sub_area, raw)
    attributes.append({'title': title, 'data': data})

    # Inferred Rocky Substrate (Area)
    title = 'Inferred Rock'
    rock_sub_area = get_sum(grid_cells, 'rck_sub_m2')
    data = format_area(rock_sub_area, raw)
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (All)
    title = 'PHS 1 for all coral and sponges'
    hsall1_m2 = get_sum(grid_cells, 'hsall1_m2')
    data = format_area(hsall1_m2, raw)
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (All)
    title = 'PHS 2 for all coral and sponges'
    hsall2_m2 = get_sum(grid_cells, 'hsall2_m2')
    data = format_area(hsall2_m2, raw)
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (All)
    title = 'PHS 3 for all coral and sponges'
    hsall3_m2 = get_sum(grid_cells, 'hsall3_m2')
    data = format_area(hsall3_m2, raw)
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (All)
    title = 'PHS 4 for all coral and sponges'
    hsall4_m2 = get_sum(grid_cells, 'hsall4_m2')
    data = format_area(hsall4_m2, raw)
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Scleractinia)
    title = 'PHS 1 for Scleractinia coral'
    hssclr1_m2 = get_sum(grid_cells, 'hssclr1_m2')
    data = format_area(hssclr1_m2, raw)
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Scleractinia)
    title = 'PHS 2 for Scleractinia coral'
    hssclr2_m2 = get_sum(grid_cells, 'hssclr2_m2')
    data = format_area(hssclr2_m2, raw)
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Scleractinia)
    title = 'PHS 3 for Scleractinia coral'
    hssclr3_m2 = get_sum(grid_cells, 'hssclr3_m2')
    data = format_area(hssclr3_m2, raw)
    attributes.append({'title': title, 'data': data})

def get_summary_reports(grid_cells, attributes):

    if grid_cells.count() == 0:
        return

    # Number of Grid Cells
    # cell_count = grid_cells.count()
    # attributes.append({'title': 'Number of Grid Cells', 'data': format(cell_count, ',d')})

    # Depth Range
    min_depth = get_min(grid_cells, 'min_fthm')
    max_depth = get_max(grid_cells, 'max_fthm')
    depth_range = '%s to %s fathoms' % (format_precision(float(min_depth), 0), format_precision(float(max_depth), 0))
    attributes.append({'title': 'Depth Range', 'data': depth_range})

    # Mean Depth
    title = 'Mean Depth'
    mean_depth = get_average(grid_cells, 'mean_fthm')
    data = str(format_precision(float(mean_depth), 0)) + ' fathoms'
    attributes.append({'title': title, 'data': data})
