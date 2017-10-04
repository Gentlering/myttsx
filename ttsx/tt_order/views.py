from django.shortcuts import render,redirect
from tt_user.user_decorators import *
from .models import *
from tt_cart.models import CartInfo
from tt_user.models import *
from django.db import transaction
from datetime import datetime
@is_login
def index(request):
    uid = request.session.get('uid')
    sites = UserAddressInfo.objects.filter(user_id=uid)
    # 修改
    site = UserAddressInfo()
    sid = request.GET.get('sid')
    if sid:
        site = UserAddressInfo.objects.get(id=sid)
    cid=request.GET.getlist("cid") #得到了一个列表[1,2,3]
    cart_list=CartInfo.objects.filter(id__in=cid)  #id_in=[1,2...]
    context={'title':'提交订单','clist':cart_list,'sites':sites,'site':site}
    return render(request,'tt_order/order.html',context)
'''
http://127.0.0.1:8000/order/?cid=1&cid=3
'''

'''
创建订单主表
查询选中的购物车信息，逐个遍历
判断商品库存是否满足当前购买数量
如果库存量不足，则事务回滚，转到购物车页面
如果库存量足够，则减少库存量，创建详单对象，删除购物车对象
计算总金额，循环结束后存储
'''
@transaction.atomic
def do_order(request):
    #接收请求的数据
    cid=request.POST.getlist('cid')
    uid=request.session.get('uid')
    #开启事务
    sid=transaction.savepoint()
    #创建订单主表类  #将时间转换为字符串strftime()
    order=OrderInfo()
    order.oid='%s%d'%(datetime.now().strftime('%Y%m%d%H%M%S'),uid)
    order.user_id=uid
    order.ototal=0
    order.oaddress=''
    order.save()
    # 查询选中的购物车信息，逐个遍历
    isok=True
    total=0
    cart_list=CartInfo.objects.filter(id__in=cid)
    for cart in cart_list:
        # 判断商品库存是否满足当前购买数量
        if cart.count<=cart.goods.gkucun:
            # 如果库存量足够
            #计算总金额
            total+=cart.count*cart.goods.gprice
            #减少库存
            cart.goods.gkucun-=cart.count
            cart.goods.save()
            #创建详单对象
            detail=OrderDetailInfo()
            detail.goods=cart.goods
            detail.order=order
            detail.price=cart.goods.gprice
            detail.count=cart.count
            detail.save()
            #删除购物车对象
            cart.delete()
        else:
            # 如果库存量不足
            isok=False
            break
    #如果正常结算退出
    if isok:
        # 保存总价
        order.ototal=total
        order.save()
        # 提交事务
        transaction.savepoint_commit(sid)
        return redirect('/user/order/')
    #k库存不足不能正常结算回到购物车页面
    else:
        #回滚事物
        transaction.savepoint_rollback(sid)
        return redirect('/cart/')



# Create your views here.
