# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('dashboard.views',
    (r'^$', 'home'),
)
