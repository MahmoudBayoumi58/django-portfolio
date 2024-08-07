from django import template

register = template.Library()


@register.filter(name='split_lines')
def split_lines(value, delimiter):
    return value.split(delimiter)
