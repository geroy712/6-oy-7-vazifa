# flowers/templatetags/flowers_tags.py

from django import template
from ..models import Tur

register = template.Library()

@register.filter
def filter_by_tur(gullar, tur_name):
    return gullar.filter(tur__nomi=tur_name)

@register.simple_tag
def all_turlar():
    return Tur.objects.all()
