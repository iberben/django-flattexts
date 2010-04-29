from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from flattexts.models import FlatText

register = template.Library()

class FlatTextNode(template.Node):
    def __init__(self, flattext_slug, var_name):
        self.flattext_slug = flattext_slug
        self.var_name = var_name

    def render(self, context):
        ftxts = FlatText.objects.filter(slug=self.flattext_slug)
        if (ftxts.count() > 0):
            context[self.var_name] = mark_safe(ftxts[0].content)
        return ''

import re
def get_flattext(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    flattext_slug, var_name = m.groups()
    if not (flattext_slug[0] == flattext_slug[-1] and flattext_slug[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return FlatTextNode(flattext_slug[1:-1], var_name)

register.tag('get_flattext', get_flattext)

