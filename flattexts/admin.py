from flattexts.models import FlatText
from django.contrib import admin

class FlatTextAdmin(admin.ModelAdmin):
	list_display = ('slug',)
	ordering = ('slug',)

admin.site.register(FlatText, FlatTextAdmin)