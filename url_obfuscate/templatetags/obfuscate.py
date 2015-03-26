# -*- coding: utf-8 -*-
from django import template
from ..helpers import obfuscate

register = template.Library()

@register.filter(name='obfuscate')
def obfuscate_url_parameter(value):
    if isinstance(value, int):
        return obfuscate(str(value).encode('utf8'))
    else:
        return obfuscate(value.encode('utf8'))
