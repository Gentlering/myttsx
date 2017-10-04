#coding=utf-8
from django.shortcuts import render
from .models import *
from tt_user.user_decorators import *
from django.http import JsonResponse
from django.db.models import Sum
@is_login
def index(request):
    uid=request.session.get('uid')
    cart_list=CartInfo.objects.filter(user_id=uid) #request.session['uid']
    context={'title':'购物车','clist':cart_list}
    return render(request,'tt_cart/cart.html',context)

'''
http://127.0.0.1:8000/order/?cid=1&cid=2
http://127.0.0.1:8000/order/?cid=1&cid=3
#被选中的checkbox才会被提交即被选中的购物车的商品才会被结算
'''
@is_login
def add(request):
    #接收请求对象
    uid=request.session.get('uid')
    dict=request.GET
    gid=int(dict.get('gid'))
    count=int(dict.get('count'))
    #构造对象
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if carts:
        cart = carts[0]
        cart.count += count
        cart.save()
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
        cart.save()
    # 返回结果
    if request.is_ajax():
        c = CartInfo.objects.filter(user_id=uid).aggregate(Sum('count'))
        return JsonResponse({'ok': 1, 'count': c.get('count__sum')})
    else:
        return redirect('/cart/')

def edit(request):
    dict = request.GET
    cid = dict.get('cid')
    count = dict.get('count')
    cart = CartInfo.objects.get(id=cid)
    cart.count = count
    cart.save()

    return JsonResponse({'ok': 1, 'count': count})

def remove(request):
    cid=request.GET.get('cid')
    cart=CartInfo.objects.get(id=cid)
    cart.delete()
    return JsonResponse({'ok':1})


def count(request):
    uid=request.session.get('uid')
    # c=CartInfo.objects.filter(user_id=uid).count()
    c=CartInfo.objects.filter(user_id=uid).aggregate(Sum('count'))
    return JsonResponse({'count':c.get('count__sum')})
# Create your views here.
