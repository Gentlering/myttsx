#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
http://127.0.0.1/user/center/?a=10
request.path======>/cilik->url/
request.get_full_path()==>/user/center/?a=10

    url('^register/$',views.register),
    url('^register_handle/$',views.register_handle),
    url(r'^active(\d+)/$',views.active),
    url('^say_hello/$',views.say_hello),
    url('^center/$',views.center),
    url('^register_name/$',views.register_name),
    url('^login/$',views.login),
    url('^login_handle/$',views.login_handle),
    url('^logout/$',views.logout),
    url('^order/$',views.order),
    url('^site/$',views.site),
    url('^islogin/$',views.islogin),
'''
class GetPathMiddleware():
    def process_view(self,request,view_func,view_args,view_kwargs):
        no_urls = [
            '/user/register/',
            '/user/register_handle/',
            '/user/register_name/',
            '/user/login/',
            '/user/login_handle/',
            '/user/logout/',
            '/user/islogin/',
        ]
        if request.path not in no_urls and 'active' not in request.path:
            request.session['url_path']=request.get_full_path()