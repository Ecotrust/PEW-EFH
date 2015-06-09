# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PlanningUnitHabitatLookup.pug'
        db.delete_column(u'scenarios_planningunithabitatlookup', 'pug_id')

        # Deleting field 'PlanningUnitHabitatLookup.sgh_id'
        db.delete_column(u'scenarios_planningunithabitatlookup', 'sgh_id')

        # Deleting field 'PlanningUnitHabitatLookup.object_id'
        db.delete_column(u'scenarios_planningunithabitatlookup', 'object_id')

        # Adding field 'PlanningUnitHabitatLookup.pug_ids'
        db.add_column(u'scenarios_planningunithabitatlookup', 'pug_ids',
                      self.gf('django.db.models.fields.TextField')(default='[]'),
                      keep_default=False)


        # Changing field 'PlanningUnitHabitatLookup.sgh_lookup_code'
        db.alter_column(u'scenarios_planningunithabitatlookup', 'sgh_lookup_code', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True))
        # Adding unique constraint on 'PlanningUnitHabitatLookup', fields ['sgh_lookup_code']
        db.create_unique(u'scenarios_planningunithabitatlookup', ['sgh_lookup_code'])


    def backwards(self, orm):
        # Removing unique constraint on 'PlanningUnitHabitatLookup', fields ['sgh_lookup_code']
        db.delete_unique(u'scenarios_planningunithabitatlookup', ['sgh_lookup_code'])

        # Adding field 'PlanningUnitHabitatLookup.pug'
        db.add_column(u'scenarios_planningunithabitatlookup', 'pug',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['scenarios.GridCell']),
                      keep_default=False)

        # Adding field 'PlanningUnitHabitatLookup.sgh_id'
        db.add_column(u'scenarios_planningunithabitatlookup', 'sgh_id',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'PlanningUnitHabitatLookup.object_id'
        db.add_column(u'scenarios_planningunithabitatlookup', 'object_id',
                      self.gf('django.db.models.fields.IntegerField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'PlanningUnitHabitatLookup.pug_ids'
        db.delete_column(u'scenarios_planningunithabitatlookup', 'pug_ids')


        # Changing field 'PlanningUnitHabitatLookup.sgh_lookup_code'
        db.alter_column(u'scenarios_planningunithabitatlookup', 'sgh_lookup_code', self.gf('django.db.models.fields.CharField')(max_length=30))

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