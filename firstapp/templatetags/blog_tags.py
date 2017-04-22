from django import template
from ..models import Artical, Category


register = template.Library()


@register.simple_tag
def archives():
    return Artical.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def archives():
    return Artical.objects.dates('created_time', 'month', order='DESC')


#