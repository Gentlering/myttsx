#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^register/$',views.register),
    url('^register_handle/$',views.register_handle),

    #注册邮箱
    url(r'^active(\d+)/$',views.active),
    url('^sayhello/$',views.sayhello),
    #用户中心
    url('^center/$',views.center),
    #注册用户
    url('^register_name/$',views.register_name),
   #登录
    url('^login/$',views.login),
    #登录验证
    url('^login_handle/$',views.login_handle),
    #退出
    url('^logout/$',views.logout),
    #订单
    url('^order/$',views.order),
    #地址
    url('^site/$',views.site),

    url('^site_handle/$', views.site_handle),
    # url('^yzm/$', views.verify_code),
    #是否登录
    url('^islogin/$',views.islogin),

]
