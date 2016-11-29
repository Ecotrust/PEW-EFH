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


def get_drawing_summary_reports(grid_cells, attributes):
    if grid_cells.count() == 0:
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
    # # Total Area
    # total_area = sum([gc.geometry.area for gc in grid_cells])
    # attributes.append({'title': 'Total Area (Drawing)', 'data': str(format_precision(float(total_area) / 2590000.0, 0)) + ' sq mi'})

    # # Depth Range
    # min_depth = get_min(grid_cells, 'depth')
    # max_depth = get_max(grid_cells, 'depth')
    # depth_range = '%s to %s fathoms' % (format_precision(float(min_depth), 0), format_precision(float(max_depth), 0))
    # attributes.append({'title': 'Depth Range (Drawing)', 'data': depth_range})

    # # Mean Depth
    # title = 'Mean Depth (Drawing)'
    # mean_depth = get_adjusted_average(grid_cells, 'depth')
    # data = str(format_precision(float(mean_depth), 0)) + ' fathoms'
    # attributes.append({'title': title, 'data': data})

    # Soft Substrate (Area)
    title = 'Soft'
    soft_sub_area = get_sum(grid_cells, 'sft_sub_m2')
    data = str(format_precision(float(soft_sub_area), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Mixed Substrate (Area)
    title = 'Mixed'
    mixed_sub_area = get_sum(grid_cells, 'mix_sub_m2')
    data = str(format_precision(float(mixed_sub_area), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Hard Substrate (Area)
    title = 'Hard'
    hard_sub_area = get_sum(grid_cells, 'hrd_sub_m2')
    data = str(format_precision(float(hard_sub_area), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Inferred Rocky Substrate (Area)
    title = 'Inferred Rock'
    rock_sub_area = get_sum(grid_cells, 'rck_sub_m2')
    data = str(format_precision(float(rock_sub_area), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (All)
    title = 'PHS 1 for all coral and sponges'
    hsall1_m2 = get_sum(grid_cells, 'hsall1_m2')
    data = str(format_precision(float(hsall1_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (All)
    title = 'PHS 2 for all coral and sponges'
    hsall2_m2 = get_sum(grid_cells, 'hsall2_m2')
    data = str(format_precision(float(hsall2_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (All)
    title = 'PHS 3 for all coral and sponges'
    hsall3_m2 = get_sum(grid_cells, 'hsall3_m2')
    data = str(format_precision(float(hsall3_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (All)
    title = 'PHS 4 for all coral and sponges'
    hsall4_m2 = get_sum(grid_cells, 'hsall4_m2')
    data = str(format_precision(float(hsall4_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Scleractinia)
    title = 'PHS 1 for Scleractinia coral'
    hssclr1_m2 = get_sum(grid_cells, 'hssclr1_m2')
    data = str(format_precision(float(hssclr1_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Scleractinia)
    title = 'PHS 2 for Scleractinia coral'
    hssclr2_m2 = get_sum(grid_cells, 'hssclr2_m2')
    data = str(format_precision(float(hssclr2_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Scleractinia)
    title = 'PHS 3 for Scleractinia coral'
    hssclr3_m2 = get_sum(grid_cells, 'hssclr3_m2')
    data = str(format_precision(float(hssclr3_m2), 0)) + ' sq mi'
    attributes.append({'title': title, 'data': data})

def get_summary_reports(grid_cells, attributes):

    if grid_cells.count() == 0:
        return

    # Number of Grid Cells
    # cell_count = grid_cells.count()
    # attributes.append({'title': 'Number of Grid Cells', 'data': format(cell_count, ',d')})
    #
    # # Total Area
    # total_area = sum([gc.geometry.area for gc in grid_cells])
    # attributes.append({'title': 'Total Area', 'data': str(format_precision(float(total_area) / 2590000.0, 0)) + ' sq mi'})

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

    # # Soft Substrate (Area)
    # title = 'Soft Substrate'
    # soft_sub_area = get_sum(grid_cells, 'sft_sub_m2')
    # data = str(format_precision(float(soft_sub_area) /  2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Mixed Substrate (Area)
    # title = 'Mixed Substrate'
    # mixed_sub_area = get_sum(grid_cells, 'mix_sub_m2')
    # data = str(format_precision(float(mixed_sub_area) /  2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Hard Substrate (Area)
    # title = 'Hard Substrate'
    # hard_sub_area = get_sum(grid_cells, 'hrd_sub_m2')
    # data = str(format_precision(float(hard_sub_area) /  2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Inferred Rocky Substrate (Area)
    # title = 'Inferred Rocky Substrate'
    # rock_sub_area = get_sum(grid_cells, 'rck_sub_m2')
    # data = str(format_precision(float(rock_sub_area) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})

    # # Coral and Sponge Presence
    # title = 'Coral & Sponge Presence'
    # cs_pres = get_sum(grid_cells, 'cnt_cs')
    # data = str(cs_pres)
    # attributes.append({'title': title, 'data': data})
    #
    # # Pennatulid Presence
    # title = 'Pennatulid Presence'
    # penn_presence = get_sum(grid_cells, 'cnt_penn')
    # data = str(penn_presence)
    # attributes.append({'title': title, 'data': data})
    #
    # # Coral and Sponge Relative Abundance
    # title = 'Coral & Sponge Relative Abundance'
    # cs_ra = get_average(grid_cells, 'ra_cs')
    # data = str(cs_ra)
    # attributes.append({'title': title, 'data': data})
    #
    # # Pennatulid Relative Abundance
    # title = 'Pennatulid Relative Abundance'
    # penn_ra = get_sum(grid_cells, 'ra_penn')
    # data = str(penn_ra)
    # attributes.append({'title': title, 'data': data})
    #
    # # Coral and Sponge Number of Observations
    # title = 'Coral/sponge observations'
    # cs_obs_sites = get_sum(grid_cells, 'cs_obs')
    # data = str(cs_obs_sites)
    # attributes.append({'title': title, 'data': data})
    #
    # # Coral and Sponge Observed Count
    # title = 'Coral/sponge specimens counted'
    # cs_spm_count = get_sum(grid_cells, 'cs_spm')
    # data = str(cs_spm_count)
    # attributes.append({'title': title, 'data': data})
    #
    # # Coral and Sponge Number of Observations Deeper than 3500m
    # title = 'Coral/sponge observations > 3500m'
    # cs3500_obs_sites = get_sum(grid_cells, 'cs3500_obs')
    # data = str(cs3500_obs_sites)
    # attributes.append({'title': title, 'data': data})
    #
    # # Coral and Sponge ObservedCount Deeper than 3500m
    # title = 'Coral/sponge specimens counted > 3500m'
    # cs3500_spm_count = get_sum(grid_cells, 'cs3500_spm')
    # data = str(cs3500_spm_count)
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (All)
    # title = 'Class 1 Suitable Habitat (All)'
    # hsall1_m2 = get_sum(grid_cells, 'hsall1_m2')
    # data = str(format_precision(float(hsall1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (All)
    # title = 'Class 2 Suitable Habitat (All)'
    # hsall2_m2 = get_sum(grid_cells, 'hsall2_m2')
    # data = str(format_precision(float(hsall2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (All)
    # title = 'Class 3 Suitable Habitat (All)'
    # hsall3_m2 = get_sum(grid_cells, 'hsall3_m2')
    # data = str(format_precision(float(hsall3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 4 Suitable Habitat (All)
    # title = 'Class 4 Suitable Habitat (All)'
    # hsall4_m2 = get_sum(grid_cells, 'hsall4_m2')
    # data = str(format_precision(float(hsall4_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (Alcyoniina)
    # title = 'Class 1 Suitable Habitat (Alcyoniina)'
    # hsalcy1_m2 = get_sum(grid_cells, 'hsalcy1_m2')
    # data = str(format_precision(float(hsalcy1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (Alcyoniina)
    # title = 'Class 2 Suitable Habitat (Alcyoniina)'
    # hsalcy2_m2 = get_sum(grid_cells, 'hsalcy2_m2')
    # data = str(format_precision(float(hsalcy2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (Alcyoniina)
    # title = 'Class 3 Suitable Habitat (Alcyoniina)'
    # hsalcy3_m2 = get_sum(grid_cells, 'hsalcy3_m2')
    # data = str(format_precision(float(hsalcy3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 4 Suitable Habitat (Alcyoniina)
    # title = 'Class 4 Suitable Habitat (Alcyoniina)'
    # hsalcy4_m2 = get_sum(grid_cells, 'hsalcy4_m2')
    # data = str(format_precision(float(hsalcy4_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (Antipatharia)
    # title = 'Class 1 Suitable Habitat (Antipatharia)'
    # hsanti1_m2 = get_sum(grid_cells, 'hsanti1_m2')
    # data = str(format_precision(float(hsanti1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (Antipatharia)
    # title = 'Class 2 Suitable Habitat (Antipatharia)'
    # hsanti2_m2 = get_sum(grid_cells, 'hsanti2_m2')
    # data = str(format_precision(float(hsanti2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (Antipatharia)
    # title = 'Class 3 Suitable Habitat (Antipatharia)'
    # hsanti3_m2 = get_sum(grid_cells, 'hsanti3_m2')
    # data = str(format_precision(float(hsanti3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (Calcaxonia)
    # title = 'Class 1 Suitable Habitat (Calcaxonia)'
    # hscalc1_m2 = get_sum(grid_cells, 'hscalc1_m2')
    # data = str(format_precision(float(hscalc1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (Calcaxonia)
    # title = 'Class 2 Suitable Habitat (Calcaxonia)'
    # hscalc2_m2 = get_sum(grid_cells, 'hscalc2_m2')
    # data = str(format_precision(float(hscalc2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (Calcaxonia)
    # title = 'Class 3 Suitable Habitat (Calcaxonia)'
    # hscalc3_m2 = get_sum(grid_cells, 'hscalc3_m2')
    # data = str(format_precision(float(hscalc3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 4 Suitable Habitat (Calcaxonia)
    # title = 'Class 4 Suitable Habitat (Calcaxonia)'
    # hscalc4_m2 = get_sum(grid_cells, 'hscalc4_m2')
    # data = str(format_precision(float(hscalc4_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (Haloxonia)
    # title = 'Class 1 Suitable Habitat (Haloxonia)'
    # hshola1_m2 = get_sum(grid_cells, 'hshola1_m2')
    # data = str(format_precision(float(hshola1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (Haloxonia)
    # title = 'Class 2 Suitable Habitat (Haloxonia)'
    # hshola2_m2 = get_sum(grid_cells, 'hshola2_m2')
    # data = str(format_precision(float(hshola2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (Haloxonia)
    # title = 'Class 3 Suitable Habitat (Haloxonia)'
    # hshola3_m2 = get_sum(grid_cells, 'hshola3_m2')
    # data = str(format_precision(float(hshola3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 4 Suitable Habitat (Haloxonia)
    # title = 'Class 4 Suitable Habitat (Haloxonia)'
    # hshola4_m2 = get_sum(grid_cells, 'hshola4_m2')
    # data = str(format_precision(float(hshola4_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (Scleractinia)
    # title = 'Class 1 Suitable Habitat (Scleractinia)'
    # hssclr1_m2 = get_sum(grid_cells, 'hssclr1_m2')
    # data = str(format_precision(float(hssclr1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (Scleractinia)
    # title = 'Class 2 Suitable Habitat (Scleractinia)'
    # hssclr2_m2 = get_sum(grid_cells, 'hssclr2_m2')
    # data = str(format_precision(float(hssclr2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (Scleractinia)
    # title = 'Class 3 Suitable Habitat (Scleractinia)'
    # hssclr3_m2 = get_sum(grid_cells, 'hssclr3_m2')
    # data = str(format_precision(float(hssclr3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 1 Suitable Habitat (Scleraxonia)
    # title = 'Class 1 Suitable Habitat (Scleraxonia)'
    # hssclx1_m2 = get_sum(grid_cells, 'hssclx1_m2')
    # data = str(format_precision(float(hssclx1_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 2 Suitable Habitat (Scleraxonia)
    # title = 'Class 2 Suitable Habitat (Scleraxonia)'
    # hssclx2_m2 = get_sum(grid_cells, 'hssclx2_m2')
    # data = str(format_precision(float(hssclx2_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 3 Suitable Habitat (Scleraxonia)
    # title = 'Class 3 Suitable Habitat (Scleraxonia)'
    # hssclx3_m2 = get_sum(grid_cells, 'hssclx3_m2')
    # data = str(format_precision(float(hssclx3_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Class 4 Suitable Habitat (Scleraxonia)
    # title = 'Class 4 Suitable Habitat (Scleraxonia)'
    # hssclx4_m2 = get_sum(grid_cells, 'hssclx4_m2')
    # data = str(format_precision(float(hssclx4_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Estuary Habitat
    # title = 'Estuary Habitat (Area)'
    # hpc_est_m2 = get_sum(grid_cells, 'hpc_est_m2')
    # data = str(format_precision(float(hpc_est_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Kelp Habitat
    # title = 'Kelp Habitat (Area)'
    # hpc_klp_m2 = get_sum(grid_cells, 'hpc_klp_m2')
    # data = str(format_precision(float(hpc_klp_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Rocky Reef Habitat
    # title = 'Rocky Reef Habitat (Area)'
    # hpc_rck_m2 = get_sum(grid_cells, 'hpc_rck_m2')
    # data = str(format_precision(float(hpc_rck_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
    #
    # # Seagrass Habitat
    # title = 'Seagrass (Area)'
    # hpc_sgr_m2 = get_sum(grid_cells, 'hpc_sgr_m2')
    # data = str(format_precision(float(hpc_sgr_m2) / 2590000.0, 0)) + ' sq mi'
    # attributes.append({'title': title, 'data': data})
