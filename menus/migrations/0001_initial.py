# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'menus_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'menus', ['Menu'])

        # Adding model 'MenuInstance'
        db.create_table(u'menus_menuinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('platform', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='menus', null=True, to=orm['platforms.Platform'])),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menus.Menu'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'menus', ['MenuInstance'])

        # Adding unique constraint on 'MenuInstance', fields ['platform', 'slug']
        db.create_unique(u'menus_menuinstance', ['platform_id', 'slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'MenuInstance', fields ['platform', 'slug']
        db.delete_unique(u'menus_menuinstance', ['platform_id', 'slug'])

        # Deleting model 'Menu'
        db.delete_table(u'menus_menu')

        # Deleting model 'MenuInstance'
        db.delete_table(u'menus_menuinstance')


    models = {
        u'menus.menu': {
            'Meta': {'object_name': 'Menu'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'menus.menuinstance': {
            'Meta': {'unique_together': "(('platform', 'slug'),)", 'object_name': 'MenuInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menus.Menu']"}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'menus'", 'null': 'True', 'to': u"orm['platforms.Platform']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'platforms.platform': {
            'Meta': {'object_name': 'Platform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['menus']