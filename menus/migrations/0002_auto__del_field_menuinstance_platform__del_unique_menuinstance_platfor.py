# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'MenuInstance', fields ['platform', 'slug']
        db.delete_unique(u'menus_menuinstance', ['platform_id', 'slug'])

        # Deleting field 'MenuInstance.platform'
        db.delete_column(u'menus_menuinstance', 'platform_id')


    def backwards(self, orm):
        # Adding field 'MenuInstance.platform'
        db.add_column(u'menus_menuinstance', 'platform',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='menus', null=True, to=orm['platforms.Platform'], blank=True),
                      keep_default=False)

        # Adding unique constraint on 'MenuInstance', fields ['platform', 'slug']
        db.create_unique(u'menus_menuinstance', ['platform_id', 'slug'])


    models = {
        u'menus.menu': {
            'Meta': {'object_name': 'Menu'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'menus.menuinstance': {
            'Meta': {'object_name': 'MenuInstance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menus.Menu']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['menus']