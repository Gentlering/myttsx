#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$',views.index),
    url('^add/$',views.add),
    url('^edit/$',views.edit),
    url('^remove/$',views.remove),
    url('^count/$', views.count),
]
