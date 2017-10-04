#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from django.shortcuts import redirect,render
from django.http import JsonResponse
#验证是否登录,未登录跳转到登录页面
def is_login(fn):
    def fun2(request,*args,**kwargs):
        if 'uid' in request.session:
            return fn(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'islogin':1})
            else:
                return redirect('/user/login/')
    return fun2
