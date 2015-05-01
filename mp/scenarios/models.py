# coding: utf-8

import os
import time
import json
from picklefield import PickledObjectField
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from madrona.common.utils import asKml
from madrona.common.jsonutils import get_properties_json, get_feature_json
from madrona.features import register
from madrona.analysistools.models import Analysis
from general.utils import miles_to_meters, feet_to_meters, meters_to_feet, mph_to_mps, mps_to_mph, format_precision
from django.contrib.gis.geos import MultiPolygon
from django.contrib.gis.db.models.aggregates import Union
from django.forms.models import model_to_dict


@register
class Scenario(Analysis):

    # min_fthm = models.BooleanField()
    # min_fthm_min = models.FloatField(null=True, blank=True)
    # min_fthm_max = models.FloatField(null=True, blank=True)
    # min_fthm_input = models.TextField(null=True, blank=True)

    mean_fthm = models.BooleanField()
    mean_fthm_min = models.FloatField(null=True, blank=True)
    mean_fthm_max = models.FloatField(null=True, blank=True)
    # mean_fthm_input = models.TextField(null=True, blank=True)

    # max_fthm = models.BooleanField()
    # max_fthm_min = models.FloatField(null=True, blank=True)
    # max_fthm_max = models.FloatField(null=True, blank=True)
    # max_fthm_input = models.TextField(null=True, blank=True)

    sft_sub_m2 = models.BooleanField()
    # sft_sub_m2_min = models.FloatField(null=True, blank=True)
    # sft_sub_m2_max = models.FloatField(null=True, blank=True)
    sft_sub_m2_input = models.TextField(null=True, blank=True)

    mix_sub_m2 = models.BooleanField()
    # mix_sub_m2_min = models.FloatField(null=True, blank=True)
    # mix_sub_m2_max = models.FloatField(null=True, blank=True)
    mix_sub_m2_input = models.TextField(null=True, blank=True)

    hrd_sub_m2 = models.BooleanField()
    # hrd_sub_m2_min = models.FloatField(null=True, blank=True)
    # hrd_sub_m2_max = models.FloatField(null=True, blank=True)
    hrd_sub_m2_input = models.TextField(null=True, blank=True)

    rck_sub_m2 = models.BooleanField()
    # rck_sub_m2_min = models.FloatField(null=True, blank=True)
    # rck_sub_m2_max = models.FloatField(null=True, blank=True)
    rck_sub_m2_input = models.TextField(null=True, blank=True)

    cnt_cs = models.BooleanField()
    # cnt_cs_min = models.FloatField(null=True, blank=True)
    # cnt_cs_max = models.FloatField(null=True, blank=True)
    cnt_cs_input = models.TextField(null=True, blank=True)

    cnt_penn = models.BooleanField()
    # cnt_penn_min = models.FloatField(null=True, blank=True)
    # cnt_penn_max = models.FloatField(null=True, blank=True)
    cnt_penn_input = models.TextField(null=True, blank=True)

    ra_cs = models.BooleanField()
    ra_cs_min = models.FloatField(null=True, blank=True)
    ra_cs_max = models.FloatField(null=True, blank=True)
    # ra_cs_input = models.TextField(null=True, blank=True)

    ra_penn = models.BooleanField()
    ra_penn_min = models.FloatField(null=True, blank=True)
    ra_penn_max = models.FloatField(null=True, blank=True)
    # ra_penn_input = models.TextField(null=True, blank=True)

    # hsalcy1_m2 = models.BooleanField()
    # hsalcy1_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy1_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy1_m2_input = models.TextField(null=True, blank=True)

    # hsalcy2_m2 = models.BooleanField()
    # hsalcy2_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy2_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy2_m2_input = models.TextField(null=True, blank=True)

    # hsalcy3_m2 = models.BooleanField()
    # hsalcy3_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy3_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy3_m2_input = models.TextField(null=True, blank=True)

    # hsalcy4_m2 = models.BooleanField()
    # hsalcy4_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy4_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy4_m2_input = models.TextField(null=True, blank=True)

    hsall1_m2 = models.BooleanField()
    hsall1_m2_min = models.FloatField(null=True, blank=True)
    hsall1_m2_max = models.FloatField(null=True, blank=True)
    # hsall1_m2_input = models.TextField(null=True, blank=True)

    hsall2_m2 = models.BooleanField()
    hsall2_m2_min = models.FloatField(null=True, blank=True)
    hsall2_m2_max = models.FloatField(null=True, blank=True)
    # hsall2_m2_input = models.TextField(null=True, blank=True)

    hsall3_m2 = models.BooleanField()
    hsall3_m2_min = models.FloatField(null=True, blank=True)
    hsall3_m2_max = models.FloatField(null=True, blank=True)
    # hsall3_m2_input = models.TextField(null=True, blank=True)

    hsall4_m2 = models.BooleanField()
    hsall4_m2_min = models.FloatField(null=True, blank=True)
    hsall4_m2_max = models.FloatField(null=True, blank=True)
    # hsall4_m2_input = models.TextField(null=True, blank=True)

    # hsanti1_m2 = models.BooleanField()
    # hsanti1_m2_min = models.FloatField(null=True, blank=True)
    # hsanti1_m2_max = models.FloatField(null=True, blank=True)
    # hsanti1_m2_input = models.TextField(null=True, blank=True)

    # hsanti2_m2 = models.BooleanField()
    # hsanti2_m2_min = models.FloatField(null=True, blank=True)
    # hsanti2_m2_max = models.FloatField(null=True, blank=True)
    # hsanti2_m2_input = models.TextField(null=True, blank=True)

    # hsanti3_m2 = models.BooleanField()
    # hsanti3_m2_min = models.FloatField(null=True, blank=True)
    # hsanti3_m2_max = models.FloatField(null=True, blank=True)
    # hsanti3_m2_input = models.TextField(null=True, blank=True)

    # hscalc1_m2 = models.BooleanField()
    # hscalc1_m2_min = models.FloatField(null=True, blank=True)
    # hscalc1_m2_max = models.FloatField(null=True, blank=True)
    # hscalc1_m2_input = models.TextField(null=True, blank=True)

    # hscalc2_m2 = models.BooleanField()
    # hscalc2_m2_min = models.FloatField(null=True, blank=True)
    # hscalc2_m2_max = models.FloatField(null=True, blank=True)
    # hscalc2_m2_input = models.TextField(null=True, blank=True)

    # hscalc3_m2 = models.BooleanField()
    # hscalc3_m2_min = models.FloatField(null=True, blank=True)
    # hscalc3_m2_max = models.FloatField(null=True, blank=True)
    # hscalc3_m2_input = models.TextField(null=True, blank=True)

    # hscalc4_m2 = models.BooleanField()
    # hscalc4_m2_min = models.FloatField(null=True, blank=True)
    # hscalc4_m2_max = models.FloatField(null=True, blank=True)
    # hscalc4_m2_input = models.TextField(null=True, blank=True)

    # hshola1_m2 = models.BooleanField()
    # hshola1_m2_min = models.FloatField(null=True, blank=True)
    # hshola1_m2_max = models.FloatField(null=True, blank=True)
    # hshola1_m2_input = models.TextField(null=True, blank=True)

    # hshola2_m2 = models.BooleanField()
    # hshola2_m2_min = models.FloatField(null=True, blank=True)
    # hshola2_m2_max = models.FloatField(null=True, blank=True)
    # hshola2_m2_input = models.TextField(null=True, blank=True)

    # hshola3_m2 = models.BooleanField()
    # hshola3_m2_min = models.FloatField(null=True, blank=True)
    # hshola3_m2_max = models.FloatField(null=True, blank=True)
    # hshola3_m2_input = models.TextField(null=True, blank=True)

    # hshola4_m2 = models.BooleanField()
    # hshola4_m2_min = models.FloatField(null=True, blank=True)
    # hshola4_m2_max = models.FloatField(null=True, blank=True)
    # hshola4_m2_input = models.TextField(null=True, blank=True)

    # hssclr1_m2 = models.BooleanField()
    # hssclr1_m2_min = models.FloatField(null=True, blank=True)
    # hssclr1_m2_max = models.FloatField(null=True, blank=True)
    # hssclr1_m2_input = models.TextField(null=True, blank=True)

    # hssclr2_m2 = models.BooleanField()
    # hssclr2_m2_min = models.FloatField(null=True, blank=True)
    # hssclr2_m2_max = models.FloatField(null=True, blank=True)
    # hssclr2_m2_input = models.TextField(null=True, blank=True)

    # hssclr3_m2 = models.BooleanField()
    # hssclr3_m2_min = models.FloatField(null=True, blank=True)
    # hssclr3_m2_max = models.FloatField(null=True, blank=True)
    # hssclr3_m2_input = models.TextField(null=True, blank=True)

    # hssclx1_m2 = models.BooleanField()
    # hssclx1_m2_min = models.FloatField(null=True, blank=True)
    # hssclx1_m2_max = models.FloatField(null=True, blank=True)
    # hssclx1_m2_input = models.TextField(null=True, blank=True)

    # hssclx2_m2 = models.BooleanField()
    # hssclx2_m2_min = models.FloatField(null=True, blank=True)
    # hssclx2_m2_max = models.FloatField(null=True, blank=True)
    # hssclx2_m2_input = models.TextField(null=True, blank=True)

    # hssclx3_m2 = models.BooleanField()
    # hssclx3_m2_min = models.FloatField(null=True, blank=True)
    # hssclx3_m2_max = models.FloatField(null=True, blank=True)
    # hssclx3_m2_input = models.TextField(null=True, blank=True)

    # hssclx4_m2 = models.BooleanField()
    # hssclx4_m2_min = models.FloatField(null=True, blank=True)
    # hssclx4_m2_max = models.FloatField(null=True, blank=True)
    # hssclx4_m2_input = models.TextField(null=True, blank=True)

    hpc_est_m2 = models.BooleanField()
    hpc_est_m2_min = models.FloatField(null=True, blank=True)
    hpc_est_m2_max = models.FloatField(null=True, blank=True)
    # hpc_est_m2_input = models.TextField(null=True, blank=True)

    hpc_klp_m2 = models.BooleanField()
    hpc_klp_m2_min = models.FloatField(null=True, blank=True)
    hpc_klp_m2_max = models.FloatField(null=True, blank=True)
    # hpc_klp_m2_input = models.TextField(null=True, blank=True)

    hpc_rck_m2 = models.BooleanField()
    hpc_rck_m2_min = models.FloatField(null=True, blank=True)
    hpc_rck_m2_max = models.FloatField(null=True, blank=True)
    # hpc_rck_m2_input = models.TextField(null=True, blank=True)

    hpc_sgr_m2 = models.BooleanField()
    hpc_sgr_m2_min = models.FloatField(null=True, blank=True)
    hpc_sgr_m2_max = models.FloatField(null=True, blank=True)
    # hpc_sgr_m2_input = models.TextField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    satisfied = models.BooleanField(default=True, help_text="Am I satisfied?")
    active = models.BooleanField(default=True)
            
    grid_cells = models.TextField(verbose_name='Grid Cell IDs', null=True, blank=True)
    geometry_final_area = models.FloatField(verbose_name='Total Area', null=True, blank=True)
    geometry_dissolved = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Filter result dissolved")
                
    @property
    def serialize_attributes(self):
        """
        Return attributes in text format. Used to display information on click in the planner. 
        """
        attributes = []

        # Step 1
        if self.mean_fthm:
            attributes.append({ 'title': 'Depth Range',
                                'data':  str(int(self.mean_fthm_min)) + ' to ' + str(int(self.mean_fthm_max)) + ' meters'})

        # Step 2

        # if self.anchor_desc:
        #     attributes.append({'title': 'Anchorage',
        #                        'data': self.anchor_desc_input})
        
        if self.sft_sub_m2:
            if self.sft_sub_m2_input == 'Y':
                title = 'Contains soft substrate'
            else:
                title = 'Does not contain any soft substrate'
            attributes.append({ 'title': title,
                                'data':  ''})


        # Step 3
        # if self.prcnt_sg:
        #     attributes.append({ 'title': 'Minimum amount of Seagrass',
        #                         'data':  str(int(self.prcnt_sg_min)) + '%'})        
        # if self.prcnt_reef:
        #     attributes.append({ 'title': 'Minimum amount of Reef',
        #                         'data':  str(int(self.prcnt_reef_min)) + '%'})       
        # if self.prcnt_sand:
        #     attributes.append({ 'title': 'Minimum amount of Sand',
        #                         'data':  str(int(self.prcnt_sand_min)) + '%'})       
        # if self.prcnt_art:
        #     attributes.append({ 'title': 'Minimum amount of Artificial Substrate',
        #                         'data':  str(int(self.prcnt_art_min)) + '%'})

        # Step 4
        # if self.fish_richness: 
        # 	attributes.append({ 'title': 'Minimum estimated fish species per survey area',
        # 						'data':  str(int(self.fish_richness_max))})

        # if self.coral_density: 
        # 	attributes.append({ 'title': 'Minimum estimated coral organisms per sq meter',
        # 						'data':  str(int(self.coral_density_max))})

        # if self.coral_richness: 
        # 	attributes.append({ 'title': 'Minimum estimated coral species per survey area',
        # 						'data':  str(int(self.coral_richness_max))})

        # if self.coral_size: 
        # 	attributes.append({ 'title': 'Minimum Coral Size',
        # 						'data':  str(int(self.coral_size_max)) + ' units'})


        # if self.coral_p or self.subveg_p or self.protarea_p:
        #     exclusions = ''
        #     if self.coral_p:
        #         exclusions += '<br>&nbsp;&nbsp; Corals'
        #     if self.subveg_p:
        #         exclusions += '<br>&nbsp;&nbsp; Submerged Vegetation'
        #     if self.protarea_p:
        #         exclusions += '<br>&nbsp;&nbsp; Protected Areas'

        #     attributes.append(dict(title='Areas containing the following were excluded', data=exclusions))        

        attributes.append({'title': 'Number of Grid Cells', 
                           'data': '{:,}'.format(self.grid_cells.count(',')+1)})
        return { 'event': 'click', 'attributes': attributes }
    
    
    def geojson(self, srid):
        props = get_properties_json(self)
        props['absolute_url'] = self.get_absolute_url()
        json_geom = self.geometry_dissolved.transform(srid, clone=True).json
        return get_feature_json(json_geom, json.dumps(props))
    

    def run(self):        
        # placing this import here to avoid circular dependency with views.py
        from views import run_filter_query
        query = run_filter_query(model_to_dict(self))

        if len(query) == 0:
            self.satisfied = False;
            # raise Exception("No lease blocks available with the current filters.")       

        dissolved_geom = query.aggregate(Union('geometry'))        
        if dissolved_geom['geometry__union']:
            dissolved_geom = dissolved_geom['geometry__union']
        else:
            raise Exception("No lease blocks available with the current filters.")
        
        if type(dissolved_geom) == MultiPolygon:
            self.geometry_dissolved = dissolved_geom
        else:
            self.geometry_dissolved = MultiPolygon(dissolved_geom, srid=dissolved_geom.srid)

        self.active = True # ??
        
        # import datetime
        # start=datetime.datetime.now()
        
        self.geometry_final_area = self.geometry_dissolved.area
        
        self.grid_cells = ','.join(str(i) 
                                     for i in query.values_list('id', flat=True))
        
        # print("Elapsed:", datetime.datetime.now() - start)
               
        if self.grid_cells == '':
            self.satisfied = False
        else:
            self.satisfied = True
        return True        
    
    def save(self, rerun=None, *args, **kwargs):
        if rerun is None and self.pk is None:
            rerun = True
        if rerun is None and self.pk is not None: #if editing a scenario and no value for rerun is given
            rerun = False
            if not rerun:
                orig = Scenario.objects.get(pk=self.pk)
                #TODO: keeping this in here til I figure out why self.grid_cells and self.geometry_final_area are emptied when run() is not called
                rerun = True
                if not rerun:
                    for f in Scenario.input_fields():
                        # Is original value different from form value?
                        if getattr(orig, f.name) != getattr(self, f.name):
                            #print 'input_field, %s, has changed' %f.name
                            rerun = True
                            break                                                                                                                   
                if not rerun:
                    '''
                        the substrates need to be grabbed, then saved, then grabbed again because 
                        both getattr calls (orig and self) return the same original list until the model has been saved 
                        (perhaps because form.save_m2m has to be called), after which calls to getattr will 
                        return the same list (regardless of whether we use orig or self)
                    ''' 
                    orig_weas = set(getattr(self, 'input_wea').all())   
                    orig_substrates = set(getattr(self, 'input_substrate').all())  
                    orig_sediments = set(getattr(self, 'input_sediment').all())                    
                    super(Scenario, self).save(rerun=False, *args, **kwargs)  
                    new_weas = set(getattr(self, 'input_wea').all())                   
                    new_substrates = set(getattr(self, 'input_substrate').all()) 
                    new_sediments = set(getattr(self, 'input_sediment').all())   
                    if orig_substrates != new_substrates or orig_sediments != new_sediments or orig_weas != new_weas:
                        rerun = True    
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)
        else: #editing a scenario and rerun is provided 
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)    
    
    def __unicode__(self):
        return u'%s' % self.name
        
    def support_filename(self):
        return os.path.basename(self.support_file.name)
        
    @classmethod
    def mapnik_geomfield(self):
        return "output_geom"

    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()
        
        ps = mapnik.PolygonSymbolizer(mapnik.Color('#ffffff'))
        ps.fill_opacity = 0.5
        
        ls = mapnik.LineSymbolizer(mapnik.Color('#555555'),0.75)
        ls.stroke_opacity = 0.5
        
        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        polygon_style.rules.append(r)
        return polygon_style     
    
    @classmethod
    def input_parameter_fields(klass):
        return [f for f in klass._meta.fields if f.attname.startswith('input_parameter_')]

    @classmethod
    def input_filter_fields(klass):
        return [f for f in klass._meta.fields if f.attname.startswith('input_filter_')]

    @property
    def grid_cells_set(self):
        if len(self.grid_cells) == 0:  #empty result
            gridcell_ids = []
        else:
            gridcell_ids = [int(id) for id in self.grid_cells.split(',')]
        gridcells = GridCell.objects.filter(pk__in=gridcell_ids)
        return gridcells
    
    @property
    def num_lease_blocks(self):
        if self.grid_cells == '':
            return 0
        return len(self.grid_cells.split(','))
    
    @property
    def geometry_is_empty(self):
        return len(self.grid_cells) == 0
    
    @property
    def input_wea_names(self):
        return [wea.wea_name for wea in self.input_wea.all()]
        
    @property
    def input_substrate_names(self):
        return [substrate.substrate_name for substrate in self.input_substrate.all()]
        
    @property
    def input_sediment_names(self):
        return [sediment.sediment_name for sediment in self.input_sediment.all()]
    
    #TODO: is this being used...?  Yes, see show.html
    @property
    def has_wind_energy_criteria(self):
        wind_parameters = Scenario.input_parameter_fields()
        for wp in wind_parameters:
            if getattr(self, wp.name):
                return True
        return False
        
    @property
    def has_shipping_filters(self):
        shipping_filters = Scenario.input_filter_fields()
        for sf in shipping_filters:
            if getattr(self, sf.name):
                return True
        return False 
        
    @property
    def has_military_filters(self):
        return False
    
    @property
    def color(self):
        try:
            return Objective.objects.get(pk=self.input_objectives.values_list()[0][0]).color
        except:
            return '778B1A55'                    
        
    @property
    def get_id(self):
        return self.id
    
    class Options:
        verbose_name = 'Spatial Design for Wind Energy'
        icon_url = 'marco/img/multi.png'
        form = 'scenarios.forms.ScenarioForm'
        form_template = 'scenario/form.html'
        show_template = 'scenario/show.html'

#no longer needed?
# class Objective(models.Model):
#     name = models.CharField(max_length=35)
#     color = models.CharField(max_length=8, default='778B1A55')
    
#     def __unicode__(self):
#         return u'%s' % self.name        

#no longer needed?
# class Parameter(models.Model):
#     ordering_id = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=35, null=True, blank=True)
#     shortname = models.CharField(max_length=35, null=True, blank=True)
#     objectives = models.ManyToManyField("Objective", null=True, blank=True)
    
#     def __unicode__(self):
#         return u'%s' % self.name


class GridCell(models.Model):

    min_fthm = models.IntegerField(null=True, blank=True)
    mean_fthm = models.IntegerField(null=True, blank=True)
    max_fthm = models.IntegerField(null=True, blank=True)
    sft_sub_m2 = models.IntegerField(null=True, blank=True)
    mix_sub_m2 = models.IntegerField(null=True, blank=True)
    hrd_sub_m2 = models.IntegerField(null=True, blank=True)
    rck_sub_m2 = models.IntegerField(null=True, blank=True)
    cnt_cs = models.IntegerField(null=True, blank=True)
    cnt_penn = models.IntegerField(null=True, blank=True)
    ra_cs = models.IntegerField(null=True, blank=True)
    ra_penn = models.IntegerField(null=True, blank=True)
    hsalcy1_m2 = models.IntegerField(null=True, blank=True)
    hsalcy2_m2 = models.IntegerField(null=True, blank=True)
    hsalcy3_m2 = models.IntegerField(null=True, blank=True)
    hsalcy4_m2 = models.IntegerField(null=True, blank=True)
    hsall1_m2 = models.IntegerField(null=True, blank=True)
    hsall2_m2 = models.IntegerField(null=True, blank=True)
    hsall3_m2 = models.IntegerField(null=True, blank=True)
    hsall4_m2 = models.IntegerField(null=True, blank=True)
    hsanti1_m2 = models.IntegerField(null=True, blank=True)
    hsanti2_m2 = models.IntegerField(null=True, blank=True)
    hsanti3_m2 = models.IntegerField(null=True, blank=True)
    hscalc1_m2 = models.IntegerField(null=True, blank=True)
    hscalc2_m2 = models.IntegerField(null=True, blank=True)
    hscalc3_m2 = models.IntegerField(null=True, blank=True)
    hscalc4_m2 = models.IntegerField(null=True, blank=True)
    hshola1_m2 = models.IntegerField(null=True, blank=True)
    hshola2_m2 = models.IntegerField(null=True, blank=True)
    hshola3_m2 = models.IntegerField(null=True, blank=True)
    hshola4_m2 = models.IntegerField(null=True, blank=True)
    hssclr1_m2 = models.IntegerField(null=True, blank=True)
    hssclr2_m2 = models.IntegerField(null=True, blank=True)
    hssclr3_m2 = models.IntegerField(null=True, blank=True)
    hssclx1_m2 = models.IntegerField(null=True, blank=True)
    hssclx2_m2 = models.IntegerField(null=True, blank=True)
    hssclx3_m2 = models.IntegerField(null=True, blank=True)
    hssclx4_m2 = models.IntegerField(null=True, blank=True)
    hpc_est_m2 = models.IntegerField(null=True, blank=True)
    hpc_klp_m2 = models.IntegerField(null=True, blank=True)
    hpc_rck_m2 = models.IntegerField(null=True, blank=True)
    hpc_sgr_m2 = models.IntegerField(null=True, blank=True)

    unique_id = models.IntegerField(null=True, blank=True)

    centroid = models.PointField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True,
        blank=True
    )

    geometry = models.MultiPolygonField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True, blank=True,
        verbose_name="Grid Cell Geometry"
    )
    objects = models.GeoManager()
