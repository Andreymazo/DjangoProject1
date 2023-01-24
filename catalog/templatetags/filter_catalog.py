from django import template
# from django.utils.html import conditional_escape
# from django.utils.safestring import mazo
register = template.Library()
@register.filter(needs_autoescape=True)
def zamena_path(path1, path2, autoescape=True):
    if autoescape:
        return path1
    return path2
