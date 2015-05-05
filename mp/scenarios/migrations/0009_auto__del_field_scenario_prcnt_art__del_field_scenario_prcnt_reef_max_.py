# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Scenario.prcnt_art'
        db.delete_column(u'scenarios_scenario', 'prcnt_art')

        # Deleting field 'Scenario.prcnt_reef_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_reef_max')

        # Deleting field 'Scenario.pillar_presence_input'
        db.delete_column(u'scenarios_scenario', 'pillar_presence_input')

        # Deleting field 'Scenario.fish_richness_min'
        db.delete_column(u'scenarios_scenario', 'fish_richness_min')

        # Deleting field 'Scenario.depth_min'
        db.delete_column(u'scenarios_scenario', 'depth_min')

        # Deleting field 'Scenario.depth_max'
        db.delete_column(u'scenarios_scenario', 'depth_max')

        # Deleting field 'Scenario.pier_distance_min'
        db.delete_column(u'scenarios_scenario', 'pier_distance_min')

        # Deleting field 'Scenario.prcnt_sg_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_sg_max')

        # Deleting field 'Scenario.inlet_distance'
        db.delete_column(u'scenarios_scenario', 'inlet_distance')

        # Deleting field 'Scenario.coral_richness_max'
        db.delete_column(u'scenarios_scenario', 'coral_richness_max')

        # Deleting field 'Scenario.prcnt_reef'
        db.delete_column(u'scenarios_scenario', 'prcnt_reef')

        # Deleting field 'Scenario.prcnt_sg'
        db.delete_column(u'scenarios_scenario', 'prcnt_sg')

        # Deleting field 'Scenario.impacted'
        db.delete_column(u'scenarios_scenario', 'impacted')

        # Deleting field 'Scenario.prcnt_sand_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_sand_max')

        # Deleting field 'Scenario.prcnt_art_max'
        db.delete_column(u'scenarios_scenario', 'prcnt_art_max')

        # Deleting field 'Scenario.shore_distance_max'
        db.delete_column(u'scenarios_scenario', 'shore_distance_max')

        # Deleting field 'Scenario.large_live_coral_input'
        db.delete_column(u'scenarios_scenario', 'large_live_coral_input')

        # Deleting field 'Scenario.outfall_distance_max'
        db.delete_column(u'scenarios_scenario', 'outfall_distance_max')

        # Deleting field 'Scenario.fish_richness_max'
        db.delete_column(u'scenarios_scenario', 'fish_richness_max')

        # Deleting field 'Scenario.injury_site'
        db.delete_column(u'scenarios_scenario', 'injury_site')

        # Deleting field 'Scenario.fish_richness'
        db.delete_column(u'scenarios_scenario', 'fish_richness')

        # Deleting field 'Scenario.mooring_buoy'
        db.delete_column(u'scenarios_scenario', 'mooring_buoy')

        # Deleting field 'Scenario.coral_richness_min'
        db.delete_column(u'scenarios_scenario', 'coral_richness_min')

        # Deleting field 'Scenario.injury_site_input'
        db.delete_column(u'scenarios_scenario', 'injury_site_input')

        # Deleting field 'Scenario.coral_richness'
        db.delete_column(u'scenarios_scenario', 'coral_richness')

        # Deleting field 'Scenario.large_live_coral'
        db.delete_column(u'scenarios_scenario', 'large_live_coral')

        # Deleting field 'Scenario.acropora_pa_input'
        db.delete_column(u'scenarios_scenario', 'acropora_pa_input')

        # Deleting field 'Scenario.inlet_distance_max'
        db.delete_column(u'scenarios_scenario', 'inlet_distance_max')

        # Deleting field 'Scenario.inlet_distance_min'
        db.delete_column(u'scenarios_scenario', 'inlet_distance_min')

        # Deleting field 'Scenario.outfall_distance_min'
        db.delete_column(u'scenarios_scenario', 'outfall_distance_min')

        # Deleting field 'Scenario.coral_density'
        db.delete_column(u'scenarios_scenario', 'coral_density')

        # Deleting field 'Scenario.shore_distance_min'
        db.delete_column(u'scenarios_scenario', 'shore_distance_min')

        # Deleting field 'Scenario.anchorage_input'
        db.delete_column(u'scenarios_scenario', 'anchorage_input')

        # Deleting field 'Scenario.outfall_distance'
        db.delete_column(u'scenarios_scenario', 'outfall_distance')

        # Deleting field 'Scenario.coral_density_max'
        db.delete_column(u'scenarios_scenario', 'coral_density_max')

        # Deleting field 'Scenario.prcnt_sg_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_sg_min')

        # Deleting field 'Scenario.coral_density_min'
        db.delete_column(u'scenarios_scenario', 'coral_density_min')

        # Deleting field 'Scenario.impacted_input'
        db.delete_column(u'scenarios_scenario', 'impacted_input')

        # Deleting field 'Scenario.coral_size_min'
        db.delete_column(u'scenarios_scenario', 'coral_size_min')

        # Deleting field 'Scenario.pier_distance'
        db.delete_column(u'scenarios_scenario', 'pier_distance')

        # Deleting field 'Scenario.pier_distance_max'
        db.delete_column(u'scenarios_scenario', 'pier_distance_max')

        # Deleting field 'Scenario.anchorage'
        db.delete_column(u'scenarios_scenario', 'anchorage')

        # Deleting field 'Scenario.prcnt_sand'
        db.delete_column(u'scenarios_scenario', 'prcnt_sand')

        # Deleting field 'Scenario.prcnt_sand_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_sand_min')

        # Deleting field 'Scenario.coral_size_max'
        db.delete_column(u'scenarios_scenario', 'coral_size_max')

        # Deleting field 'Scenario.prcnt_reef_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_reef_min')

        # Deleting field 'Scenario.acropora_pa'
        db.delete_column(u'scenarios_scenario', 'acropora_pa')

        # Deleting field 'Scenario.shore_distance'
        db.delete_column(u'scenarios_scenario', 'shore_distance')

        # Deleting field 'Scenario.depth'
        db.delete_column(u'scenarios_scenario', 'depth')

        # Deleting field 'Scenario.coral_size'
        db.delete_column(u'scenarios_scenario', 'coral_size')

        # Deleting field 'Scenario.pillar_presence'
        db.delete_column(u'scenarios_scenario', 'pillar_presence')

        # Deleting field 'Scenario.mooring_buoy_input'
        db.delete_column(u'scenarios_scenario', 'mooring_buoy_input')

        # Deleting field 'Scenario.prcnt_art_min'
        db.delete_column(u'scenarios_scenario', 'prcnt_art_min')

        # Adding field 'Scenario.min_fthm'
        db.add_column(u'scenarios_scenario', 'min_fthm',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mean_fthm'
        db.add_column(u'scenarios_scenario', 'mean_fthm',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mean_fthm_min'
        db.add_column(u'scenarios_scenario', 'mean_fthm_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.mean_fthm_max'
        db.add_column(u'scenarios_scenario', 'mean_fthm_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.max_fthm'
        db.add_column(u'scenarios_scenario', 'max_fthm',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.sft_sub_m2'
        db.add_column(u'scenarios_scenario', 'sft_sub_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.sft_sub_m2_input'
        db.add_column(u'scenarios_scenario', 'sft_sub_m2_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.mix_sub_m2'
        db.add_column(u'scenarios_scenario', 'mix_sub_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mix_sub_m2_input'
        db.add_column(u'scenarios_scenario', 'mix_sub_m2_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hrd_sub_m2'
        db.add_column(u'scenarios_scenario', 'hrd_sub_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hrd_sub_m2_input'
        db.add_column(u'scenarios_scenario', 'hrd_sub_m2_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.rck_sub_m2'
        db.add_column(u'scenarios_scenario', 'rck_sub_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.rck_sub_m2_input'
        db.add_column(u'scenarios_scenario', 'rck_sub_m2_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.cnt_cs'
        db.add_column(u'scenarios_scenario', 'cnt_cs',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.cnt_cs_input'
        db.add_column(u'scenarios_scenario', 'cnt_cs_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.cnt_penn'
        db.add_column(u'scenarios_scenario', 'cnt_penn',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.cnt_penn_input'
        db.add_column(u'scenarios_scenario', 'cnt_penn_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.ra_cs'
        db.add_column(u'scenarios_scenario', 'ra_cs',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.ra_penn'
        db.add_column(u'scenarios_scenario', 'ra_penn',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsalcy1_m2'
        db.add_column(u'scenarios_scenario', 'hsalcy1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsalcy2_m2'
        db.add_column(u'scenarios_scenario', 'hsalcy2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsalcy3_m2'
        db.add_column(u'scenarios_scenario', 'hsalcy3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsalcy4_m2'
        db.add_column(u'scenarios_scenario', 'hsalcy4_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsall1_m2'
        db.add_column(u'scenarios_scenario', 'hsall1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsall1_m2_min'
        db.add_column(u'scenarios_scenario', 'hsall1_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall1_m2_max'
        db.add_column(u'scenarios_scenario', 'hsall1_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall2_m2'
        db.add_column(u'scenarios_scenario', 'hsall2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsall2_m2_min'
        db.add_column(u'scenarios_scenario', 'hsall2_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall2_m2_max'
        db.add_column(u'scenarios_scenario', 'hsall2_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall3_m2'
        db.add_column(u'scenarios_scenario', 'hsall3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsall3_m2_min'
        db.add_column(u'scenarios_scenario', 'hsall3_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall3_m2_max'
        db.add_column(u'scenarios_scenario', 'hsall3_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall4_m2'
        db.add_column(u'scenarios_scenario', 'hsall4_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsall4_m2_min'
        db.add_column(u'scenarios_scenario', 'hsall4_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsall4_m2_max'
        db.add_column(u'scenarios_scenario', 'hsall4_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hsanti1_m2'
        db.add_column(u'scenarios_scenario', 'hsanti1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsanti2_m2'
        db.add_column(u'scenarios_scenario', 'hsanti2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hsanti3_m2'
        db.add_column(u'scenarios_scenario', 'hsanti3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hscalc1_m2'
        db.add_column(u'scenarios_scenario', 'hscalc1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hscalc2_m2'
        db.add_column(u'scenarios_scenario', 'hscalc2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hscalc3_m2'
        db.add_column(u'scenarios_scenario', 'hscalc3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hscalc4_m2'
        db.add_column(u'scenarios_scenario', 'hscalc4_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hshola1_m2'
        db.add_column(u'scenarios_scenario', 'hshola1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hshola2_m2'
        db.add_column(u'scenarios_scenario', 'hshola2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hshola3_m2'
        db.add_column(u'scenarios_scenario', 'hshola3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hshola4_m2'
        db.add_column(u'scenarios_scenario', 'hshola4_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclr1_m2'
        db.add_column(u'scenarios_scenario', 'hssclr1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclr2_m2'
        db.add_column(u'scenarios_scenario', 'hssclr2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclr3_m2'
        db.add_column(u'scenarios_scenario', 'hssclr3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclx1_m2'
        db.add_column(u'scenarios_scenario', 'hssclx1_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclx2_m2'
        db.add_column(u'scenarios_scenario', 'hssclx2_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclx3_m2'
        db.add_column(u'scenarios_scenario', 'hssclx3_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hssclx4_m2'
        db.add_column(u'scenarios_scenario', 'hssclx4_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hpc_est_m2'
        db.add_column(u'scenarios_scenario', 'hpc_est_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hpc_est_m2_min'
        db.add_column(u'scenarios_scenario', 'hpc_est_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_est_m2_max'
        db.add_column(u'scenarios_scenario', 'hpc_est_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_klp_m2'
        db.add_column(u'scenarios_scenario', 'hpc_klp_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hpc_klp_m2_min'
        db.add_column(u'scenarios_scenario', 'hpc_klp_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_klp_m2_max'
        db.add_column(u'scenarios_scenario', 'hpc_klp_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_rck_m2'
        db.add_column(u'scenarios_scenario', 'hpc_rck_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hpc_rck_m2_min'
        db.add_column(u'scenarios_scenario', 'hpc_rck_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_rck_m2_max'
        db.add_column(u'scenarios_scenario', 'hpc_rck_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_sgr_m2'
        db.add_column(u'scenarios_scenario', 'hpc_sgr_m2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.hpc_sgr_m2_min'
        db.add_column(u'scenarios_scenario', 'hpc_sgr_m2_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.hpc_sgr_m2_max'
        db.add_column(u'scenarios_scenario', 'hpc_sgr_m2_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Scenario.prcnt_art'
        db.add_column(u'scenarios_scenario', 'prcnt_art',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_reef_max'
        db.add_column(u'scenarios_scenario', 'prcnt_reef_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.pillar_presence_input'
        db.add_column(u'scenarios_scenario', 'pillar_presence_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.fish_richness_min'
        db.add_column(u'scenarios_scenario', 'fish_richness_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth_min'
        db.add_column(u'scenarios_scenario', 'depth_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.depth_max'
        db.add_column(u'scenarios_scenario', 'depth_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.pier_distance_min'
        db.add_column(u'scenarios_scenario', 'pier_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sg_max'
        db.add_column(u'scenarios_scenario', 'prcnt_sg_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.inlet_distance'
        db.add_column(u'scenarios_scenario', 'inlet_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_richness_max'
        db.add_column(u'scenarios_scenario', 'coral_richness_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_reef'
        db.add_column(u'scenarios_scenario', 'prcnt_reef',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sg'
        db.add_column(u'scenarios_scenario', 'prcnt_sg',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.impacted'
        db.add_column(u'scenarios_scenario', 'impacted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sand_max'
        db.add_column(u'scenarios_scenario', 'prcnt_sand_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_art_max'
        db.add_column(u'scenarios_scenario', 'prcnt_art_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.shore_distance_max'
        db.add_column(u'scenarios_scenario', 'shore_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.large_live_coral_input'
        db.add_column(u'scenarios_scenario', 'large_live_coral_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.outfall_distance_max'
        db.add_column(u'scenarios_scenario', 'outfall_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.fish_richness_max'
        db.add_column(u'scenarios_scenario', 'fish_richness_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.injury_site'
        db.add_column(u'scenarios_scenario', 'injury_site',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.fish_richness'
        db.add_column(u'scenarios_scenario', 'fish_richness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mooring_buoy'
        db.add_column(u'scenarios_scenario', 'mooring_buoy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_richness_min'
        db.add_column(u'scenarios_scenario', 'coral_richness_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.injury_site_input'
        db.add_column(u'scenarios_scenario', 'injury_site_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_richness'
        db.add_column(u'scenarios_scenario', 'coral_richness',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.large_live_coral'
        db.add_column(u'scenarios_scenario', 'large_live_coral',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.acropora_pa_input'
        db.add_column(u'scenarios_scenario', 'acropora_pa_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.inlet_distance_max'
        db.add_column(u'scenarios_scenario', 'inlet_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.inlet_distance_min'
        db.add_column(u'scenarios_scenario', 'inlet_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.outfall_distance_min'
        db.add_column(u'scenarios_scenario', 'outfall_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_density'
        db.add_column(u'scenarios_scenario', 'coral_density',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.shore_distance_min'
        db.add_column(u'scenarios_scenario', 'shore_distance_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.anchorage_input'
        db.add_column(u'scenarios_scenario', 'anchorage_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.outfall_distance'
        db.add_column(u'scenarios_scenario', 'outfall_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_density_max'
        db.add_column(u'scenarios_scenario', 'coral_density_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sg_min'
        db.add_column(u'scenarios_scenario', 'prcnt_sg_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_density_min'
        db.add_column(u'scenarios_scenario', 'coral_density_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.impacted_input'
        db.add_column(u'scenarios_scenario', 'impacted_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_size_min'
        db.add_column(u'scenarios_scenario', 'coral_size_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.pier_distance'
        db.add_column(u'scenarios_scenario', 'pier_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.pier_distance_max'
        db.add_column(u'scenarios_scenario', 'pier_distance_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.anchorage'
        db.add_column(u'scenarios_scenario', 'anchorage',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sand'
        db.add_column(u'scenarios_scenario', 'prcnt_sand',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_sand_min'
        db.add_column(u'scenarios_scenario', 'prcnt_sand_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.coral_size_max'
        db.add_column(u'scenarios_scenario', 'coral_size_max',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_reef_min'
        db.add_column(u'scenarios_scenario', 'prcnt_reef_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.acropora_pa'
        db.add_column(u'scenarios_scenario', 'acropora_pa',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.shore_distance'
        db.add_column(u'scenarios_scenario', 'shore_distance',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.depth'
        db.add_column(u'scenarios_scenario', 'depth',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.coral_size'
        db.add_column(u'scenarios_scenario', 'coral_size',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.pillar_presence'
        db.add_column(u'scenarios_scenario', 'pillar_presence',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Scenario.mooring_buoy_input'
        db.add_column(u'scenarios_scenario', 'mooring_buoy_input',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scenario.prcnt_art_min'
        db.add_column(u'scenarios_scenario', 'prcnt_art_min',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Scenario.min_fthm'
        db.delete_column(u'scenarios_scenario', 'min_fthm')

        # Deleting field 'Scenario.mean_fthm'
        db.delete_column(u'scenarios_scenario', 'mean_fthm')

        # Deleting field 'Scenario.mean_fthm_min'
        db.delete_column(u'scenarios_scenario', 'mean_fthm_min')

        # Deleting field 'Scenario.mean_fthm_max'
        db.delete_column(u'scenarios_scenario', 'mean_fthm_max')

        # Deleting field 'Scenario.max_fthm'
        db.delete_column(u'scenarios_scenario', 'max_fthm')

        # Deleting field 'Scenario.sft_sub_m2'
        db.delete_column(u'scenarios_scenario', 'sft_sub_m2')

        # Deleting field 'Scenario.sft_sub_m2_input'
        db.delete_column(u'scenarios_scenario', 'sft_sub_m2_input')

        # Deleting field 'Scenario.mix_sub_m2'
        db.delete_column(u'scenarios_scenario', 'mix_sub_m2')

        # Deleting field 'Scenario.mix_sub_m2_input'
        db.delete_column(u'scenarios_scenario', 'mix_sub_m2_input')

        # Deleting field 'Scenario.hrd_sub_m2'
        db.delete_column(u'scenarios_scenario', 'hrd_sub_m2')

        # Deleting field 'Scenario.hrd_sub_m2_input'
        db.delete_column(u'scenarios_scenario', 'hrd_sub_m2_input')

        # Deleting field 'Scenario.rck_sub_m2'
        db.delete_column(u'scenarios_scenario', 'rck_sub_m2')

        # Deleting field 'Scenario.rck_sub_m2_input'
        db.delete_column(u'scenarios_scenario', 'rck_sub_m2_input')

        # Deleting field 'Scenario.cnt_cs'
        db.delete_column(u'scenarios_scenario', 'cnt_cs')

        # Deleting field 'Scenario.cnt_cs_input'
        db.delete_column(u'scenarios_scenario', 'cnt_cs_input')

        # Deleting field 'Scenario.cnt_penn'
        db.delete_column(u'scenarios_scenario', 'cnt_penn')

        # Deleting field 'Scenario.cnt_penn_input'
        db.delete_column(u'scenarios_scenario', 'cnt_penn_input')

        # Deleting field 'Scenario.ra_cs'
        db.delete_column(u'scenarios_scenario', 'ra_cs')

        # Deleting field 'Scenario.ra_penn'
        db.delete_column(u'scenarios_scenario', 'ra_penn')

        # Deleting field 'Scenario.hsalcy1_m2'
        db.delete_column(u'scenarios_scenario', 'hsalcy1_m2')

        # Deleting field 'Scenario.hsalcy2_m2'
        db.delete_column(u'scenarios_scenario', 'hsalcy2_m2')

        # Deleting field 'Scenario.hsalcy3_m2'
        db.delete_column(u'scenarios_scenario', 'hsalcy3_m2')

        # Deleting field 'Scenario.hsalcy4_m2'
        db.delete_column(u'scenarios_scenario', 'hsalcy4_m2')

        # Deleting field 'Scenario.hsall1_m2'
        db.delete_column(u'scenarios_scenario', 'hsall1_m2')

        # Deleting field 'Scenario.hsall1_m2_min'
        db.delete_column(u'scenarios_scenario', 'hsall1_m2_min')

        # Deleting field 'Scenario.hsall1_m2_max'
        db.delete_column(u'scenarios_scenario', 'hsall1_m2_max')

        # Deleting field 'Scenario.hsall2_m2'
        db.delete_column(u'scenarios_scenario', 'hsall2_m2')

        # Deleting field 'Scenario.hsall2_m2_min'
        db.delete_column(u'scenarios_scenario', 'hsall2_m2_min')

        # Deleting field 'Scenario.hsall2_m2_max'
        db.delete_column(u'scenarios_scenario', 'hsall2_m2_max')

        # Deleting field 'Scenario.hsall3_m2'
        db.delete_column(u'scenarios_scenario', 'hsall3_m2')

        # Deleting field 'Scenario.hsall3_m2_min'
        db.delete_column(u'scenarios_scenario', 'hsall3_m2_min')

        # Deleting field 'Scenario.hsall3_m2_max'
        db.delete_column(u'scenarios_scenario', 'hsall3_m2_max')

        # Deleting field 'Scenario.hsall4_m2'
        db.delete_column(u'scenarios_scenario', 'hsall4_m2')

        # Deleting field 'Scenario.hsall4_m2_min'
        db.delete_column(u'scenarios_scenario', 'hsall4_m2_min')

        # Deleting field 'Scenario.hsall4_m2_max'
        db.delete_column(u'scenarios_scenario', 'hsall4_m2_max')

        # Deleting field 'Scenario.hsanti1_m2'
        db.delete_column(u'scenarios_scenario', 'hsanti1_m2')

        # Deleting field 'Scenario.hsanti2_m2'
        db.delete_column(u'scenarios_scenario', 'hsanti2_m2')

        # Deleting field 'Scenario.hsanti3_m2'
        db.delete_column(u'scenarios_scenario', 'hsanti3_m2')

        # Deleting field 'Scenario.hscalc1_m2'
        db.delete_column(u'scenarios_scenario', 'hscalc1_m2')

        # Deleting field 'Scenario.hscalc2_m2'
        db.delete_column(u'scenarios_scenario', 'hscalc2_m2')

        # Deleting field 'Scenario.hscalc3_m2'
        db.delete_column(u'scenarios_scenario', 'hscalc3_m2')

        # Deleting field 'Scenario.hscalc4_m2'
        db.delete_column(u'scenarios_scenario', 'hscalc4_m2')

        # Deleting field 'Scenario.hshola1_m2'
        db.delete_column(u'scenarios_scenario', 'hshola1_m2')

        # Deleting field 'Scenario.hshola2_m2'
        db.delete_column(u'scenarios_scenario', 'hshola2_m2')

        # Deleting field 'Scenario.hshola3_m2'
        db.delete_column(u'scenarios_scenario', 'hshola3_m2')

        # Deleting field 'Scenario.hshola4_m2'
        db.delete_column(u'scenarios_scenario', 'hshola4_m2')

        # Deleting field 'Scenario.hssclr1_m2'
        db.delete_column(u'scenarios_scenario', 'hssclr1_m2')

        # Deleting field 'Scenario.hssclr2_m2'
        db.delete_column(u'scenarios_scenario', 'hssclr2_m2')

        # Deleting field 'Scenario.hssclr3_m2'
        db.delete_column(u'scenarios_scenario', 'hssclr3_m2')

        # Deleting field 'Scenario.hssclx1_m2'
        db.delete_column(u'scenarios_scenario', 'hssclx1_m2')

        # Deleting field 'Scenario.hssclx2_m2'
        db.delete_column(u'scenarios_scenario', 'hssclx2_m2')

        # Deleting field 'Scenario.hssclx3_m2'
        db.delete_column(u'scenarios_scenario', 'hssclx3_m2')

        # Deleting field 'Scenario.hssclx4_m2'
        db.delete_column(u'scenarios_scenario', 'hssclx4_m2')

        # Deleting field 'Scenario.hpc_est_m2'
        db.delete_column(u'scenarios_scenario', 'hpc_est_m2')

        # Deleting field 'Scenario.hpc_est_m2_min'
        db.delete_column(u'scenarios_scenario', 'hpc_est_m2_min')

        # Deleting field 'Scenario.hpc_est_m2_max'
        db.delete_column(u'scenarios_scenario', 'hpc_est_m2_max')

        # Deleting field 'Scenario.hpc_klp_m2'
        db.delete_column(u'scenarios_scenario', 'hpc_klp_m2')

        # Deleting field 'Scenario.hpc_klp_m2_min'
        db.delete_column(u'scenarios_scenario', 'hpc_klp_m2_min')

        # Deleting field 'Scenario.hpc_klp_m2_max'
        db.delete_column(u'scenarios_scenario', 'hpc_klp_m2_max')

        # Deleting field 'Scenario.hpc_rck_m2'
        db.delete_column(u'scenarios_scenario', 'hpc_rck_m2')

        # Deleting field 'Scenario.hpc_rck_m2_min'
        db.delete_column(u'scenarios_scenario', 'hpc_rck_m2_min')

        # Deleting field 'Scenario.hpc_rck_m2_max'
        db.delete_column(u'scenarios_scenario', 'hpc_rck_m2_max')

        # Deleting field 'Scenario.hpc_sgr_m2'
        db.delete_column(u'scenarios_scenario', 'hpc_sgr_m2')

        # Deleting field 'Scenario.hpc_sgr_m2_min'
        db.delete_column(u'scenarios_scenario', 'hpc_sgr_m2_min')

        # Deleting field 'Scenario.hpc_sgr_m2_max'
        db.delete_column(u'scenarios_scenario', 'hpc_sgr_m2_max')


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
            'hssclx1_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx2_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx3_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hssclx4_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_fthm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mean_fthm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_fthm': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mix_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ra_cs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ra_penn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rck_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sft_sub_m2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'scenarios.scenario': {
            'Meta': {'object_name': 'Scenario'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cnt_cs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cnt_cs_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cnt_penn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cnt_penn_input': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'scenarios_scenario_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
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
            'hsanti1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsanti2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsanti3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'hssclx1_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx2_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx3_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hssclx4_m2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_fthm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mean_fthm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mean_fthm_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mean_fthm_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_fthm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'scenarios_scenario_related'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['scenarios']