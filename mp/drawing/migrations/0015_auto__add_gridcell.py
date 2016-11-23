# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GridCell'
        db.create_table(u'drawing_gridcell', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gridcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sq_mi', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hrd_sub_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('mix_sub_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('sft_sub_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('rck_sub_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('depth', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hsall1_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hsall2_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hsall3_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hsall4_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hssclr1_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hssclr2_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('hssclr3_m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('flag1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('shape_length', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=16, decimal_places=11, blank=True)),
            ('unique_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('centroid', self.gf('django.contrib.gis.db.models.fields.PointField')(srid=3857, null=True, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=3857, null=True, blank=True)),
        ))
        db.send_create_signal(u'drawing', ['GridCell'])


    def backwards(self, orm):
        # Deleting model 'GridCell'
        db.delete_table(u'drawing_gridcell')


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
        u'drawing.aoi': {
            'Meta': {'object_name': 'AOI'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'drawing_aoi_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geometry_final': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'geometry_orig': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manipulators': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'drawing_aoi_related'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'drawing_aoi_related'", 'to': u"orm['auth.User']"})
        },
        u'drawing.collection': {
            'Meta': {'object_name': 'Collection'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'drawing_collection_related'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sharing_groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'drawing_collection_related'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'drawing_collection_related'", 'to': u"orm['auth.User']"})
        },
        u'drawing.gridcell': {
            'Meta': {'object_name': 'GridCell'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'flag1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857', 'null': 'True', 'blank': 'True'}),
            'gridcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hrd_sub_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hsall1_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hsall2_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hsall3_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hsall4_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hssclr1_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hssclr2_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'hssclr3_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mix_sub_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'rck_sub_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'sft_sub_m2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'shape_length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'sq_mi': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '11', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['drawing']