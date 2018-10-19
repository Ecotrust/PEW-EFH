# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GridCell.min_fthm'
        db.add_column(u'scenarios_gridcell', 'min_fthm',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mean_fthm'
        db.add_column(u'scenarios_gridcell', 'mean_fthm',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.max_fthm'
        db.add_column(u'scenarios_gridcell', 'max_fthm',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.cnt_cs'
        db.add_column(u'scenarios_gridcell', 'cnt_cs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.cnt_penn'
        db.add_column(u'scenarios_gridcell', 'cnt_penn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.ra_cs'
        db.add_column(u'scenarios_gridcell', 'ra_cs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.ra_penn'
        db.add_column(u'scenarios_gridcell', 'ra_penn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.cs_obs'
        db.add_column(u'scenarios_gridcell', 'cs_obs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.cs_spm'
        db.add_column(u'scenarios_gridcell', 'cs_spm',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.cs3500_obs'
        db.add_column(u'scenarios_gridcell', 'cs3500_obs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.cs3500_spm'
        db.add_column(u'scenarios_gridcell', 'cs3500_spm',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.sft_sub_m2'
        db.add_column(u'scenarios_gridcell', 'sft_sub_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mix_sub_m2'
        db.add_column(u'scenarios_gridcell', 'mix_sub_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hrd_sub_m2'
        db.add_column(u'scenarios_gridcell', 'hrd_sub_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.rck_sub_m2'
        db.add_column(u'scenarios_gridcell', 'rck_sub_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hpc_est_m2'
        db.add_column(u'scenarios_gridcell', 'hpc_est_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hpc_klp_m2'
        db.add_column(u'scenarios_gridcell', 'hpc_klp_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hpc_rck_m2'
        db.add_column(u'scenarios_gridcell', 'hpc_rck_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hpc_sgr_m2'
        db.add_column(u'scenarios_gridcell', 'hpc_sgr_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsalcy1_m2'
        db.add_column(u'scenarios_gridcell', 'hsalcy1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsalcy2_m2'
        db.add_column(u'scenarios_gridcell', 'hsalcy2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsalcy3_m2'
        db.add_column(u'scenarios_gridcell', 'hsalcy3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsalcy4_m2'
        db.add_column(u'scenarios_gridcell', 'hsalcy4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsall1_m2'
        db.add_column(u'scenarios_gridcell', 'hsall1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsall2_m2'
        db.add_column(u'scenarios_gridcell', 'hsall2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsall3_m2'
        db.add_column(u'scenarios_gridcell', 'hsall3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsall4_m2'
        db.add_column(u'scenarios_gridcell', 'hsall4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsanti1_m2'
        db.add_column(u'scenarios_gridcell', 'hsanti1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsanti2_m2'
        db.add_column(u'scenarios_gridcell', 'hsanti2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsanti3_m2'
        db.add_column(u'scenarios_gridcell', 'hsanti3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hsanti4_m2'
        db.add_column(u'scenarios_gridcell', 'hsanti4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hscalc1_m2'
        db.add_column(u'scenarios_gridcell', 'hscalc1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hscalc2_m2'
        db.add_column(u'scenarios_gridcell', 'hscalc2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hscalc3_m2'
        db.add_column(u'scenarios_gridcell', 'hscalc3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hscalc4_m2'
        db.add_column(u'scenarios_gridcell', 'hscalc4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hshola1_m2'
        db.add_column(u'scenarios_gridcell', 'hshola1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hshola2_m2'
        db.add_column(u'scenarios_gridcell', 'hshola2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hshola3_m2'
        db.add_column(u'scenarios_gridcell', 'hshola3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hshola4_m2'
        db.add_column(u'scenarios_gridcell', 'hshola4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclr1_m2'
        db.add_column(u'scenarios_gridcell', 'hssclr1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclr2_m2'
        db.add_column(u'scenarios_gridcell', 'hssclr2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclr3_m2'
        db.add_column(u'scenarios_gridcell', 'hssclr3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclr4_m2'
        db.add_column(u'scenarios_gridcell', 'hssclr4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclx1_m2'
        db.add_column(u'scenarios_gridcell', 'hssclx1_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclx2_m2'
        db.add_column(u'scenarios_gridcell', 'hssclx2_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclx3_m2'
        db.add_column(u'scenarios_gridcell', 'hssclx3_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.hssclx4_m2'
        db.add_column(u'scenarios_gridcell', 'hssclx4_m2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'GridCell.region'
        db.delete_column(u'scenarios_gridcell', 'region')

        # Deleting field 'GridCell.county'
        db.delete_column(u'scenarios_gridcell', 'county')

        # Deleting field 'GridCell.fish_density'
        db.delete_column(u'scenarios_gridcell', 'fish_density')

        # Deleting field 'GridCell.fish_div'
        db.delete_column(u'scenarios_gridcell', 'fish_div')

        # Deleting field 'GridCell.fish_richness'
        db.delete_column(u'scenarios_gridcell', 'fish_richness')

        # Deleting field 'GridCell.coral_bleach'
        db.delete_column(u'scenarios_gridcell', 'coral_bleach')

        # Deleting field 'GridCell.coral_cover'
        db.delete_column(u'scenarios_gridcell', 'coral_cover')

        # Deleting field 'GridCell.coral_density'
        db.delete_column(u'scenarios_gridcell', 'coral_density')

        # Deleting field 'GridCell.coral_richness'
        db.delete_column(u'scenarios_gridcell', 'coral_richness')

        # Deleting field 'GridCell.coral_size'
        db.delete_column(u'scenarios_gridcell', 'coral_size')

        # Deleting field 'GridCell.inlet_distance'
        db.delete_column(u'scenarios_gridcell', 'inlet_distance')

        # Deleting field 'GridCell.outfall_distance'
        db.delete_column(u'scenarios_gridcell', 'outfall_distance')

        # Deleting field 'GridCell.pier_distance'
        db.delete_column(u'scenarios_gridcell', 'pier_distance')

        # Deleting field 'GridCell.shore_distance'
        db.delete_column(u'scenarios_gridcell', 'shore_distance')

        # Deleting field 'GridCell.boat_use'
        db.delete_column(u'scenarios_gridcell', 'boat_use')

        # Deleting field 'GridCell.dive_use'
        db.delete_column(u'scenarios_gridcell', 'dive_use')

        # Deleting field 'GridCell.fish_use'
        db.delete_column(u'scenarios_gridcell', 'fish_use')

        # Deleting field 'GridCell.rec_use'
        db.delete_column(u'scenarios_gridcell', 'rec_use')

        # Deleting field 'GridCell.acropora_pa'
        db.delete_column(u'scenarios_gridcell', 'acropora_pa')

        # Deleting field 'GridCell.esa_spp'
        db.delete_column(u'scenarios_gridcell', 'esa_spp')

        # Deleting field 'GridCell.injury_site'
        db.delete_column(u'scenarios_gridcell', 'injury_site')

        # Deleting field 'GridCell.large_live_coral'
        db.delete_column(u'scenarios_gridcell', 'large_live_coral')

        # Deleting field 'GridCell.lionfish'
        db.delete_column(u'scenarios_gridcell', 'lionfish')

        # Deleting field 'GridCell.depth_min'
        db.delete_column(u'scenarios_gridcell', 'depth_min')

        # Deleting field 'GridCell.depth_max'
        db.delete_column(u'scenarios_gridcell', 'depth_max')

        # Deleting field 'GridCell.depth_mean'
        db.delete_column(u'scenarios_gridcell', 'depth_mean')

        # Deleting field 'GridCell.acerv_area'
        db.delete_column(u'scenarios_gridcell', 'acerv_area')

        # Deleting field 'GridCell.art_area'
        db.delete_column(u'scenarios_gridcell', 'art_area')

        # Deleting field 'GridCell.reef_area'
        db.delete_column(u'scenarios_gridcell', 'reef_area')

        # Deleting field 'GridCell.sand_area'
        db.delete_column(u'scenarios_gridcell', 'sand_area')

        # Deleting field 'GridCell.sg_area'
        db.delete_column(u'scenarios_gridcell', 'sg_area')

        # Deleting field 'GridCell.major_habitat'
        db.delete_column(u'scenarios_gridcell', 'major_habitat')

        # Deleting field 'GridCell.pillar_presence'
        db.delete_column(u'scenarios_gridcell', 'pillar_presence')

        # Deleting field 'GridCell.anchorage'
        db.delete_column(u'scenarios_gridcell', 'anchorage')

        # Deleting field 'GridCell.mooring_buoy'
        db.delete_column(u'scenarios_gridcell', 'mooring_buoy')

        # Deleting field 'GridCell.impacted'
        db.delete_column(u'scenarios_gridcell', 'impacted')

        # Deleting field 'GridCell.prcnt_sg'
        db.delete_column(u'scenarios_gridcell', 'prcnt_sg')

        # Deleting field 'GridCell.prcnt_reef'
        db.delete_column(u'scenarios_gridcell', 'prcnt_reef')

        # Deleting field 'GridCell.prcnt_sand'
        db.delete_column(u'scenarios_gridcell', 'prcnt_sand')

        # Deleting field 'GridCell.prcnt_art'
        db.delete_column(u'scenarios_gridcell', 'prcnt_art')

    def backwards(self, orm):
        # Deleting field 'GridCell.min_fthm'
        db.delete_column(u'scenarios_gridcell', 'min_fthm')

        # Deleting field 'GridCell.mean_fthm'
        db.delete_column(u'scenarios_gridcell', 'mean_fthm')

        # Deleting field 'GridCell.max_fthm'
        db.delete_column(u'scenarios_gridcell', 'max_fthm')

        # Deleting field 'GridCell.cnt_cs'
        db.delete_column(u'scenarios_gridcell', 'cnt_cs')

        # Deleting field 'GridCell.cnt_penn'
        db.delete_column(u'scenarios_gridcell', 'cnt_penn')

        # Deleting field 'GridCell.ra_cs'
        db.delete_column(u'scenarios_gridcell', 'ra_cs')

        # Deleting field 'GridCell.ra_penn'
        db.delete_column(u'scenarios_gridcell', 'ra_penn')

        # Deleting field 'GridCell.cs_obs'
        db.delete_column(u'scenarios_gridcell', 'cs_obs')

        # Deleting field 'GridCell.cs_spm'
        db.delete_column(u'scenarios_gridcell', 'cs_spm')

        # Deleting field 'GridCell.cs3500_obs'
        db.delete_column(u'scenarios_gridcell', 'cs3500_obs')

        # Deleting field 'GridCell.cs3500_spm'
        db.delete_column(u'scenarios_gridcell', 'cs3500_spm')

        # Deleting field 'GridCell.sft_sub_m2'
        db.delete_column(u'scenarios_gridcell', 'sft_sub_m2')

        # Deleting field 'GridCell.mix_sub_m2'
        db.delete_column(u'scenarios_gridcell', 'mix_sub_m2')

        # Deleting field 'GridCell.hrd_sub_m2'
        db.delete_column(u'scenarios_gridcell', 'hrd_sub_m2')

        # Deleting field 'GridCell.rck_sub_m2'
        db.delete_column(u'scenarios_gridcell', 'rck_sub_m2')

        # Deleting field 'GridCell.hpc_est_m2'
        db.delete_column(u'scenarios_gridcell', 'hpc_est_m2')

        # Deleting field 'GridCell.hpc_klp_m2'
        db.delete_column(u'scenarios_gridcell', 'hpc_klp_m2')

        # Deleting field 'GridCell.hpc_rck_m2'
        db.delete_column(u'scenarios_gridcell', 'hpc_rck_m2')

        # Deleting field 'GridCell.hpc_sgr_m2'
        db.delete_column(u'scenarios_gridcell', 'hpc_sgr_m2')

        # Deleting field 'GridCell.hsalcy1_m2'
        db.delete_column(u'scenarios_gridcell', 'hsalcy1_m2')

        # Deleting field 'GridCell.hsalcy2_m2'
        db.delete_column(u'scenarios_gridcell', 'hsalcy2_m2')

        # Deleting field 'GridCell.hsalcy3_m2'
        db.delete_column(u'scenarios_gridcell', 'hsalcy3_m2')

        # Deleting field 'GridCell.hsalcy4_m2'
        db.delete_column(u'scenarios_gridcell', 'hsalcy4_m2')

        # Deleting field 'GridCell.hsall1_m2'
        db.delete_column(u'scenarios_gridcell', 'hsall1_m2')

        # Deleting field 'GridCell.hsall2_m2'
        db.delete_column(u'scenarios_gridcell', 'hsall2_m2')

        # Deleting field 'GridCell.hsall3_m2'
        db.delete_column(u'scenarios_gridcell', 'hsall3_m2')

        # Deleting field 'GridCell.hsall4_m2'
        db.delete_column(u'scenarios_gridcell', 'hsall4_m2')

        # Deleting field 'GridCell.hsanti1_m2'
        db.delete_column(u'scenarios_gridcell', 'hsanti1_m2')

        # Deleting field 'GridCell.hsanti2_m2'
        db.delete_column(u'scenarios_gridcell', 'hsanti2_m2')

        # Deleting field 'GridCell.hsanti3_m2'
        db.delete_column(u'scenarios_gridcell', 'hsanti3_m2')

        # Deleting field 'GridCell.hsanti4_m2'
        db.delete_column(u'scenarios_gridcell', 'hsanti4_m2')

        # Deleting field 'GridCell.hscalc1_m2'
        db.delete_column(u'scenarios_gridcell', 'hscalc1_m2')

        # Deleting field 'GridCell.hscalc2_m2'
        db.delete_column(u'scenarios_gridcell', 'hscalc2_m2')

        # Deleting field 'GridCell.hscalc3_m2'
        db.delete_column(u'scenarios_gridcell', 'hscalc3_m2')

        # Deleting field 'GridCell.hscalc4_m2'
        db.delete_column(u'scenarios_gridcell', 'hscalc4_m2')

        # Deleting field 'GridCell.hshola1_m2'
        db.delete_column(u'scenarios_gridcell', 'hshola1_m2')

        # Deleting field 'GridCell.hshola2_m2'
        db.delete_column(u'scenarios_gridcell', 'hshola2_m2')

        # Deleting field 'GridCell.hshola3_m2'
        db.delete_column(u'scenarios_gridcell', 'hshola3_m2')

        # Deleting field 'GridCell.hshola4_m2'
        db.delete_column(u'scenarios_gridcell', 'hshola4_m2')

        # Deleting field 'GridCell.hssclr1_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclr1_m2')

        # Deleting field 'GridCell.hssclr2_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclr2_m2')

        # Deleting field 'GridCell.hssclr3_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclr3_m2')

        # Deleting field 'GridCell.hssclr4_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclr4_m2')

        # Deleting field 'GridCell.hssclx1_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclx1_m2')

        # Deleting field 'GridCell.hssclx2_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclx2_m2')

        # Deleting field 'GridCell.hssclx3_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclx3_m2')

        # Deleting field 'GridCell.hssclx4_m2'
        db.delete_column(u'scenarios_gridcell', 'hssclx4_m2')

        # Adding field 'GridCell.region'
        db.add_column(u'scenarios_gridcell', 'region',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.county'
        db.add_column(u'scenarios_gridcell', 'county',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.fish_density'
        db.add_column(u'scenarios_gridcell', 'fish_density',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.fish_div'
        db.add_column(u'scenarios_gridcell', 'fish_div',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.fish_richness'
        db.add_column(u'scenarios_gridcell', 'fish_richness',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_bleach'
        db.add_column(u'scenarios_gridcell', 'coral_bleach',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_cover'
        db.add_column(u'scenarios_gridcell', 'coral_cover',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_density'
        db.add_column(u'scenarios_gridcell', 'coral_density',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_richness'
        db.add_column(u'scenarios_gridcell', 'coral_richness',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.coral_size'
        db.add_column(u'scenarios_gridcell', 'coral_size',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.inlet_distance'
        db.add_column(u'scenarios_gridcell', 'inlet_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.outfall_distance'
        db.add_column(u'scenarios_gridcell', 'outfall_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.pier_distance'
        db.add_column(u'scenarios_gridcell', 'pier_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.shore_distance'
        db.add_column(u'scenarios_gridcell', 'shore_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.boat_use'
        db.add_column(u'scenarios_gridcell', 'boat_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.dive_use'
        db.add_column(u'scenarios_gridcell', 'dive_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.fish_use'
        db.add_column(u'scenarios_gridcell', 'fish_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.rec_use'
        db.add_column(u'scenarios_gridcell', 'rec_use',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.acropora_pa'
        db.add_column(u'scenarios_gridcell', 'acropora_pa',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.esa_spp'
        db.add_column(u'scenarios_gridcell', 'esa_spp',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.injury_site'
        db.add_column(u'scenarios_gridcell', 'injury_site',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.large_live_coral'
        db.add_column(u'scenarios_gridcell', 'large_live_coral',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.lionfish'
        db.add_column(u'scenarios_gridcell', 'lionfish',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.depth_min'
        db.add_column(u'scenarios_gridcell', 'depth_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.depth_max'
        db.add_column(u'scenarios_gridcell', 'depth_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.depth_mean'
        db.add_column(u'scenarios_gridcell', 'depth_mean',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.acerv_area'
        db.add_column(u'scenarios_gridcell', 'acerv_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.art_area'
        db.add_column(u'scenarios_gridcell', 'art_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.reef_area'
        db.add_column(u'scenarios_gridcell', 'reef_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.sand_area'
        db.add_column(u'scenarios_gridcell', 'sand_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.sg_area'
        db.add_column(u'scenarios_gridcell', 'sg_area',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.major_habitat'
        db.add_column(u'scenarios_gridcell', 'major_habitat',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.pillar_presence'
        db.add_column(u'scenarios_gridcell', 'pillar_presence',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.anchorage'
        db.add_column(u'scenarios_gridcell', 'anchorage',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.mooring_buoy'
        db.add_column(u'scenarios_gridcell', 'mooring_buoy',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.impacted'
        db.add_column(u'scenarios_gridcell', 'impacted',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_sg'
        db.add_column(u'scenarios_gridcell', 'prcnt_sg',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_reef'
        db.add_column(u'scenarios_gridcell', 'prcnt_reef',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_sand'
        db.add_column(u'scenarios_gridcell', 'prcnt_sand',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'GridCell.prcnt_art'
        db.add_column(u'scenarios_gridcell', 'prcnt_art',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'scenarios.gridcell': {
            'Meta': {'object_name': 'GridCell'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'cnt_cs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cnt_penn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cs3500_obs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cs3500_spm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cs_obs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cs_spm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'hpc_est_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_klp_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_rck_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_sgr_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hrd_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsalcy1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsalcy2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsalcy3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsalcy4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsall1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsall2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsall3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsall4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsanti1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsanti2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsanti3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hsanti4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hscalc1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hscalc2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hscalc3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hscalc4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hshola1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hshola2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hshola3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hshola4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclr1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclr2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclr3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclr4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_fthm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_meter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_fthm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_meter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_fthm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_meter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mix_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ra_cs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ra_penn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rck_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sft_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'scenarios.planningunithabitatlookup': {
            'Meta': {'object_name': 'PlanningUnitHabitatLookup'},
            'pug_ids': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'sgh_lookup_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'})
        },
        u'scenarios.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cnt_cs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cnt_cs_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cnt_penn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cnt_penn_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'cs3500_obs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cs3500_obs_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cs3500_spm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cs3500_spm_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cs_obs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cs_obs_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cs_spm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cs_spm_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_dissolved': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'geometry_final_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'grid_cells': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_est_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hpc_est_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_est_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_klp_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hpc_klp_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_klp_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_rck_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hpc_rck_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_rck_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_sgr_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hpc_sgr_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hpc_sgr_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hrd_sub_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hrd_sub_m2_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hsalcy1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsalcy2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsalcy3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsalcy4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsall1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsall1_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall1_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsall2_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall2_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsall3_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall3_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsall4_m2_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall4_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsall_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsall_m2_checkboxes': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hsall_m2_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hsanti1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsanti2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsanti3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsanti4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hscalc1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hscalc2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hscalc3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hscalc4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hshola1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hshola2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hshola3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hshola4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclr1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclr2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclr3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclr4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lifestage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lifestage_input': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'max_fthm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_meter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mean_fthm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mean_fthm_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mean_fthm_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mean_meter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mean_meter_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_meter_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_fthm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'min_meter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mix_sub_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mix_sub_m2_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ra_cs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ra_penn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rck_sub_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rck_sub_m2_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'satisfied': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sft_sub_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sft_sub_m2_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            'species': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'species_input': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'scenarios_scenario_related'", 'to': u"orm['auth.User']"})
        },
        u'scenarios.species': {
            'Meta': {'object_name': 'Species'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'scenarios.specieshabitatoccurence': {
            'Meta': {'object_name': 'SpeciesHabitatOccurence'},
            'absolute_max_depth': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_min_depth': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'activity_association': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'habitat_association': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'level_1_habitat': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'level_2_habitat': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'level_3_habitat': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'level_4_habitat': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'lifestage': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'preferred_max_depth': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'preferred_min_depth': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sgh_lookup_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'species_common': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'species_sci': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xwalk_sgh': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['scenarios']
