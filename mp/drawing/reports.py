from general.utils import format_precision

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
            max = gc.depth_max
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
    sum = 0
    for gc in grid_cells:
        sum += getattr(gc, field)
    return sum 

def get_average(grid_cells, field):
    cell_count = grid_cells.count()
    if cell_count == 0:
        return 0
    sum = get_sum(grid_cells, field)
    return sum / cell_count

def get_unique_values(grid_cells, field):
    values = []
    for gc in grid_cells:
        value = getattr(gc, field)
        if value not in values:
            values.append(value)
    return values


def get_summary_reports(grid_cells, attributes):

    if grid_cells.count() == 0:
        return

    # Number of Grid Cells
    cell_count = grid_cells.count()
    attributes.append({'title': 'Number of Grid Cells', 'data': format(cell_count, ',d')})

    # Total Area
    total_area = sum([gc.geometry.area for gc in grid_cells])
    attributes.append({'title': 'Total Area', 'data': str(format_precision(total_area / 1000000, 2)) + ' sq km'})

    # Depth Range
    min_depth = get_min(grid_cells, 'min_fthm')
    max_depth = get_max(grid_cells, 'max_fthm')
    depth_range = '%s to %s fathoms' % (format_precision(min_depth, 0), format_precision(max_depth, 0))
    attributes.append({'title': 'Depth Range', 'data': depth_range})

    # Mean Depth
    title = 'Mean Depth'
    mean_depth = get_average(grid_cells, 'mean_fthm')
    data = str(format_precision(mean_depth, 2)) + ' fathoms'
    attributes.append({'title': title, 'data': data})

    # Soft Substrate (Area)
    title = 'Soft Substrate'
    soft_sub_area = get_sum(grid_cells, 'sft_sub_m2')
    data = str(format_precision(soft_sub_area / 1000000.0, 2)) + ' sq km'
    attributes.append({'title': title, 'data': data})

    # Mixed Substrate (Area)
    title = 'Mixed Substrate'
    mixed_sub_area = get_sum(grid_cells, 'mix_sub_m2')
    data = str(format_precision(mixed_sub_area / 1000000.0, 2)) + ' sq km'
    attributes.append({'title': title, 'data': data})

    # Hard Substrate (Area)
    title = 'Hard Substrate'
    hard_sub_area = get_sum(grid_cells, 'hrd_sub_m2')
    data = str(format_precision(hard_sub_area / 1000000.0, 2)) + ' sq km'
    attributes.append({'title': title, 'data': data})

    # Inferred Rocky Substrate (Area)
    title = 'Inferred Rocky Substrate'
    rock_sub_area = get_sum(grid_cells, 'rck_sub_m2')
    data = str(format_precision(rock_sub_area / 1000000.0, 2)) + ' sq km'
    attributes.append({'title': title, 'data': data})

    # Coral and Sponge Presence
    title = 'Coral & Sponge Presence'
    cs_pres = get_sum(grid_cells, 'cnt_cs')
    data = str(cs_pres)
    attributes.append({'title': title, 'data': data})

    # Pennatulid Presence
    title = 'Pennatulid Presence'
    penn_presence = get_sum(grid_cells, 'cnt_penn')
    data = str(penn_presence)
    attributes.append({'title': title, 'data': data})

    # Coral and Sponge Relative Abundance
    title = 'Coral & Sponge Relative Abundance'
    cs_ra = get_average(grid_cells, 'ra_cs')
    data = str(cs_ra)
    attributes.append({'title': title, 'data': data})

    # Pennatulid Relative Abundance
    title = 'Pennatulid Relative Abundance'
    penn_ra = get_sum(grid_cells, 'ra_penn')
    data = str(penn_ra)
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (All)
    title = 'Class 1 Suitable Habitat (All)'
    hsall1_m2 = get_sum(grid_cells, 'hsall1_m2')
    data = str(format_precision(hsall1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (All)
    title = 'Class 2 Suitable Habitat (All)'
    hsall2_m2 = get_sum(grid_cells, 'hsall2_m2')
    data = str(format_precision(hsall2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (All)
    title = 'Class 3 Suitable Habitat (All)'
    hsall3_m2 = get_sum(grid_cells, 'hsall3_m2')
    data = str(format_precision(hsall3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (All)
    title = 'Class 4 Suitable Habitat (All)'
    hsall4_m2 = get_sum(grid_cells, 'hsall4_m2')
    data = str(format_precision(hsall4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Alcyoniina)
    title = 'Class 1 Suitable Habitat (Alcyoniina)'
    hsalcy1_m2 = get_sum(grid_cells, 'hsalcy1_m2')
    data = str(format_precision(hsalcy1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Alcyoniina)
    title = 'Class 2 Suitable Habitat (Alcyoniina)'
    hsalcy2_m2 = get_sum(grid_cells, 'hsalcy2_m2')
    data = str(format_precision(hsalcy2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Alcyoniina)
    title = 'Class 3 Suitable Habitat (Alcyoniina)'
    hsalcy3_m2 = get_sum(grid_cells, 'hsalcy3_m2')
    data = str(format_precision(hsalcy3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (Alcyoniina)
    title = 'Class 4 Suitable Habitat (Alcyoniina)'
    hsalcy4_m2 = get_sum(grid_cells, 'hsalcy4_m2')
    data = str(format_precision(hsalcy4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Antipatharia)
    title = 'Class 1 Suitable Habitat (Antipatharia)'
    hsanti1_m2 = get_sum(grid_cells, 'hsanti1_m2')
    data = str(format_precision(hsanti1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Antipatharia)
    title = 'Class 2 Suitable Habitat (Antipatharia)'
    hsanti2_m2 = get_sum(grid_cells, 'hsanti2_m2')
    data = str(format_precision(hsanti2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Antipatharia)
    title = 'Class 3 Suitable Habitat (Antipatharia)'
    hsanti3_m2 = get_sum(grid_cells, 'hsanti3_m2')
    data = str(format_precision(hsanti3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (Antipatharia)
    title = 'Class 4 Suitable Habitat (Antipatharia)'
    hsanti4_m2 = get_sum(grid_cells, 'hsanti4_m2')
    data = str(format_precision(hsanti4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Calcaxonia)
    title = 'Class 1 Suitable Habitat (Calcaxonia)'
    hscalc1_m2 = get_sum(grid_cells, 'hscalc1_m2')
    data = str(format_precision(hscalc1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Calcaxonia)
    title = 'Class 2 Suitable Habitat (Calcaxonia)'
    hscalc2_m2 = get_sum(grid_cells, 'hscalc2_m2')
    data = str(format_precision(hscalc2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Calcaxonia)
    title = 'Class 3 Suitable Habitat (Calcaxonia)'
    hscalc3_m2 = get_sum(grid_cells, 'hscalc3_m2')
    data = str(format_precision(hscalc3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (Calcaxonia)
    title = 'Class 4 Suitable Habitat (Calcaxonia)'
    hscalc4_m2 = get_sum(grid_cells, 'hscalc4_m2')
    data = str(format_precision(hscalc4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Haloxonia)
    title = 'Class 1 Suitable Habitat (Haloxonia)'
    hshola1_m2 = get_sum(grid_cells, 'hshola1_m2')
    data = str(format_precision(hshola1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Haloxonia)
    title = 'Class 2 Suitable Habitat (Haloxonia)'
    hshola2_m2 = get_sum(grid_cells, 'hshola2_m2')
    data = str(format_precision(hshola2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Haloxonia)
    title = 'Class 3 Suitable Habitat (Haloxonia)'
    hshola3_m2 = get_sum(grid_cells, 'hshola3_m2')
    data = str(format_precision(hshola3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (Haloxonia)
    title = 'Class 4 Suitable Habitat (Haloxonia)'
    hshola4_m2 = get_sum(grid_cells, 'hshola4_m2')
    data = str(format_precision(hshola4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Scleractinia)
    title = 'Class 1 Suitable Habitat (Scleractinia)'
    hssclr1_m2 = get_sum(grid_cells, 'hssclr1_m2')
    data = str(format_precision(hssclr1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Scleractinia)
    title = 'Class 2 Suitable Habitat (Scleractinia)'
    hssclr2_m2 = get_sum(grid_cells, 'hssclr2_m2')
    data = str(format_precision(hssclr2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Scleractinia)
    title = 'Class 3 Suitable Habitat (Scleractinia)'
    hssclr3_m2 = get_sum(grid_cells, 'hssclr3_m2')
    data = str(format_precision(hssclr3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (Scleractinia)
    title = 'Class 4 Suitable Habitat (Scleractinia)'
    hssclr4_m2 = get_sum(grid_cells, 'hssclr4_m2')
    data = str(format_precision(hssclr4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 1 Suitable Habitat (Scleraxonia)
    title = 'Class 1 Suitable Habitat (Scleraxonia)'
    hssclx1_m2 = get_sum(grid_cells, 'hssclx1_m2')
    data = str(format_precision(hssclx1_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 2 Suitable Habitat (Scleraxonia)
    title = 'Class 2 Suitable Habitat (Scleraxonia)'
    hssclx2_m2 = get_sum(grid_cells, 'hssclx2_m2')
    data = str(format_precision(hssclx2_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 3 Suitable Habitat (Scleraxonia)
    title = 'Class 3 Suitable Habitat (Scleraxonia)'
    hssclx3_m2 = get_sum(grid_cells, 'hssclx3_m2')
    data = str(format_precision(hssclx3_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Class 4 Suitable Habitat (Scleraxonia)
    title = 'Class 4 Suitable Habitat (Scleraxonia)'
    hssclx4_m2 = get_sum(grid_cells, 'hssclx4_m2')
    data = str(format_precision(hssclx4_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Estuary Habitat
    title = 'Estuary Habitat (Area)'
    hpc_est_m2 = get_sum(grid_cells, 'hpc_est_m2')
    data = str(format_precision(hpc_est_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Kelp Habitat
    title = 'Kelp Habitat (Area)'
    hpc_klp_m2 = get_sum(grid_cells, 'hpc_klp_m2')
    data = str(format_precision(hpc_klp_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Rocky Reef Habitat
    title = 'Rocky Reef Habitat (Area)'
    hpc_rck_m2 = get_sum(grid_cells, 'hpc_rck_m2')
    data = str(format_precision(hpc_rck_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})

    # Seagrass Habitat
    title = 'Seagrass (Area)'
    hpc_sgr_m2 = get_sum(grid_cells, 'hpc_sgr_m2')
    data = str(format_precision(hpc_sgr_m2 / 1000000.0, 2) + ' sq km')
    attributes.append({'title': title, 'data': data})
