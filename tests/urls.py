# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from url_obfuscate.helpers import generate_url_pattern

urlpatterns = patterns('views',
    url(generate_url_pattern('/'), 'home', name='home'),
    url(generate_url_pattern('obfuscated_link', params=['(?P<name>[^/]+)']), 'obfuscated_link', name='obfuscated_link'),
    url(generate_url_pattern('optional_param', params=['(?:(?P<param>[^/]+)/)?']), 'optional_param', name='optional_param'),
)
