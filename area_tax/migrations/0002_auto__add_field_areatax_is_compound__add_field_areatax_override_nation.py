# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'AreaTax.is_compound'
        db.add_column('area_tax_areatax', 'is_compound', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'AreaTax.override_national'
        db.add_column('area_tax_areatax', 'override_national', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding unique constraint on 'AreaTax', fields ['country', 'area']
        db.create_unique('area_tax_areatax', ['country_id', 'area_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AreaTax', fields ['country', 'area']
        db.delete_unique('area_tax_areatax', ['country_id', 'area_id'])

        # Deleting field 'AreaTax.is_compound'
        db.delete_column('area_tax_areatax', 'is_compound')

        # Deleting field 'AreaTax.override_national'
        db.delete_column('area_tax_areatax', 'override_national')


    models = {
        'area_tax.areatax': {
            'Meta': {'unique_together': "(('country', 'area'),)", 'object_name': 'AreaTax'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.AdminArea']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'override_national': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'l10n.adminarea': {
            'Meta': {'ordering': "('name',)", 'object_name': 'AdminArea'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'l10n.country': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin_area': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso2_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'iso3_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['area_tax']
