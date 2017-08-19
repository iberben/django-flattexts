# import re

from django import template
# from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from flattexts.models import FlatText

register = template.Library()


@register.simple_tag
def get_flattext(key, *args, **kwargs):
    try:
        ftxt = FlatText.objects.get(slug=key)
        return mark_safe(ftxt.content)
    except FlatText.DoesNotExist:
        pass
    return ''
