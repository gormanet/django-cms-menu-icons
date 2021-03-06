# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IconExtension'
        db.create_table('cms_menu_icons_iconextension', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public_extension', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms_menu_icons.IconExtension'], null=True, related_name='draft_extension', unique=True)),
            ('extended_object', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.Page'], unique=True)),
            ('menu_icon_font_awesome', self.gf('django.db.models.fields.CharField')(blank=True, default='icon-', null=True, max_length=48)),
            ('menu_icon_image', self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100)),
            ('menu_icon_url', self.gf('django.db.models.fields.URLField')(blank=True, null=True, max_length=200)),
        ))
        db.send_create_signal('cms_menu_icons', ['IconExtension'])


    def backwards(self, orm):
        # Deleting model 'IconExtension'
        db.delete_table('cms_menu_icons_iconextension')


    models = {
        'cms.page': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'unique_together': "(('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'object_name': 'Page'},
            'application_namespace': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True', 'max_length': '80'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'blank': 'True', 'related_name': "'children'", 'null': 'True'}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.Page']", 'null': 'True', 'related_name': "'publisher_draft'", 'unique': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'blank': 'True', 'null': 'True', 'max_length': '40'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'related_name': "'djangocms_pages'"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'xframe_options': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'})
        },
        'cms_menu_icons.iconextension': {
            'Meta': {'object_name': 'IconExtension'},
            'extended_object': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.Page']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_icon_font_awesome': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'icon-'", 'null': 'True', 'max_length': '48'}),
            'menu_icon_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'menu_icon_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'public_extension': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms_menu_icons.IconExtension']", 'null': 'True', 'related_name': "'draft_extension'", 'unique': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'", 'ordering': "('domain',)", 'object_name': 'Site'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['cms_menu_icons']