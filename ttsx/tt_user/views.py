from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from hashlib import sha1
from django.core.mail import send_mail
from django.conf import settings
from . import task
import time
from .user_decorators import *
from tt_goods.models import *
from tt_order.models import *
from django.core.paginator import Paginator,Page
# Create your views here.
def register(request):
    context={'title':'用户注册'}
    return render(request,'tt_user/register.html',context)

def register_handle(request):
    #接收请求的数据
    dict=request.POST
    uname=dict.get('user_name')
    upwd=dict.get('pwd')
    uemail=dict.get('email')
    #密码加密（sha1）
    s1=sha1()
    s1.update(upwd.encode('utf-8'))
    upwd_sha1=s1.hexdigest()

    #创建对象并保存
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd_sha1
    user.uemail=uemail
    user.save()
    #发送邮件
    # msg='<a href="http://127.0.0.1:8000/user/active%s/">点击激活</a>'%(user.id)
    # send_mail('天天生鲜,注册用户激活','',settings.EMAIL_FROM,[uemail],html_message=msg)
    #提示
    task.sendmail.delay(user.id,uemail)
    return HttpResponse('邮箱已发送,请到注册的邮箱中激活！')

def active(request,uid):
    #找到用户对象
    user=UserInfo.objects.get(id=uid)
    #激活，修改属性
    user.isActive=True
    user.save()
    return HttpResponse('用户已激活, <a href="/user/login/">点击登录</a>')

def sayhello(request):
    # print("hello django")
    # time.sleep(2)
    # print("bye django")
    #将任务加入celery中
    # task.sayhello.delay()
    task.sayhello.delay()
    return HttpResponse("over")
#验证是否登录,未登录跳转到登录页面
@is_login
def center(request):
    # if 'uid' in request.session:
    #     context={'title':'用户中心'}
    #     return render(request,'tt_user/user_center_info.html',context)
    # else:
    #     return redirect('/user/login/')
    zjll = request.COOKIES.get('zjll', '')
    uid = request.session.get('uid')
    sites = UserAddressInfo.objects.filter(user_id=uid)
    # 修改
    site = UserAddressInfo()
    sid = request.GET.get('sid')
    if sid:
        site = UserAddressInfo.objects.get(id=sid)
    goods_list = []
    if zjll:
        zjll_list = zjll.split(',')
        for gid in zjll_list:
            goods_list.append(GoodsInfo.objects.get(id=gid))
    context={'title':'用户中心','goods_list':goods_list,'sites':sites,'site':site}
    return render(request,'tt_user/user_center_info.html',context)

@is_login
def order(request):
    uid=request.session.get('uid')
    pindex=request.GET.get('page','1')
    order_list=OrderInfo.objects.filter(user_id=uid).order_by('-odate')
    paginator=Paginator(order_list,2)
    page=paginator.page(int(pindex))
    context = {'title': '我的订单','page':page}
    return render(request, 'tt_user/user_center_order.html', context)
@is_login
def site(request):
    uid=request.session.get('uid')
    sites=UserAddressInfo.objects.filter(user_id=uid)
    #修改
    site=UserAddressInfo()
    sid=request.GET.get('sid')
    if sid:
        site=UserAddressInfo.objects.get(id=sid)
    context={'title':'收货地址','sites':sites,'site':site,}
    return render(request,'tt_user/user_center_site.html',context)

@is_login
def site_handle(request):
    dict=request.POST
    uid=request.session.get('uid')
    sid=dict.get('sid')
    uname=dict.get('uname')
    uaddress=dict.get('uaddress')
    uphone=dict.get('uphone')

    if sid=='0':#新增
        address=UserAddressInfo()
    else:#修改
        address=UserAddressInfo.objects.get(id=sid)

    address.uname = uname
    address.uphone = uphone
    address.uaddress = uaddress
    address.user_id = uid
    address.save()

    return redirect('/user/site/')

def islogin(request):
    ok=0
    if 'uid' in request.session:
        ok=1
    return JsonResponse({'ok':ok})

def register_name(request):
    #接收请求的用户名
    uname=request.GET.get('uname')
    #查询用户名
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('user_name', '')
    context = {'title': '用户登录', 'uname': uname}
    return render(request,'tt_user/login.html',context)

def login_handle(request):
    #接收请求的用户名，密码
    dict=request.POST
    uname=dict.get("username")
    upwd=dict.get('pwd')
    urem=dict.get('rem','0')

    # 构造返回的上下文
    context = {'title': '登录', 'uname': uname, 'upwd': upwd}

    #构造用户名查询对象
    user=UserInfo.objects.filter(uname=uname,isActive=True,isValid=True)
    if user:
        #用户名存在
        upwd_db=user[0].upwd
        # 对请求的密码加密
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        upwd_sha1 = s1.hexdigest()
        # 判断密码是否正确
        if upwd_db == upwd_sha1:
            # 密码正确,登录成功
            response = redirect(request.session.get('url_path', '/'))
            # 记住用户名
            if urem == "1":
                response.set_cookie('user_name', uname, expires=60 * 60 * 24 * 14)
            else:
                response.set_cookie('user_name', '', expires=-1)
            # 记录登录状态
            request.session['uid'] = user[0].id
            request.session['uname'] = uname

            return response
        else:
            # 密码错误
            context['upwd_error'] = 1
            return render(request, 'tt_user/login.html', context)
    else:
        # 用户名不存在
        context['uname_error'] = 1
        return render(request, 'tt_user/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

