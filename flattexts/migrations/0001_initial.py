
from south.db import db
from django.db import models
from flattexts.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'FlatText'
        db.create_table('flattexts_flattext', (
            ('id', orm['flattexts.FlatText:id']),
            ('slug', orm['flattexts.FlatText:slug']),
            ('content', orm['flattexts.FlatText:content']),
        ))
        db.send_create_signal('flattexts', ['FlatText'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'FlatText'
        db.delete_table('flattexts_flattext')
        
    
    
    models = {
        'flattexts.flattext': {
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['flattexts']
