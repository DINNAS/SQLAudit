# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('dashboard.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
)
