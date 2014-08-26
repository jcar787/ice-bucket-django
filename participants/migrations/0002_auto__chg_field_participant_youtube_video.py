# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Participant.youtube_video'
        db.alter_column(u'participants_participant', 'youtube_video', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Participant.youtube_video'
        db.alter_column(u'participants_participant', 'youtube_video', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'participants.participant': {
            'Meta': {'object_name': 'Participant'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_did_challenge': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'youtube_video': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['participants']