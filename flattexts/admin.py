from flattexts.models import FlatText
from django.contrib import admin
from django.db import models

from parler.admin import TranslatableAdmin

from django_summernote.widgets import SummernoteWidget


class FlatTextAdmin(TranslatableAdmin):
    list_display = ('slug',)
    ordering = ('slug',)
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }
admin.site.register(FlatText, FlatTextAdmin)
