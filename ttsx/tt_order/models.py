#coding=utf-8
from django.db import models

class OrderInfo(models.Model):
    oid=models.CharField(max_length=20, primary_key=True)
    #订单用户
    user=models.ForeignKey('tt_user.UserInfo')
    #下单日期
    odate=models.DateTimeField(auto_now_add=True)
    #是否支付
    oIsPay=models.BooleanField(default=False)
    #金额总计
    ototal=models.DecimalField(max_digits=6,decimal_places=2)
    #收货地址
    oaddress=models.CharField(max_length=150)

class OrderDetailInfo(models.Model):
    #商品类
    goods=models.ForeignKey('tt_goods.GoodsInfo')
    #订单类
    order=models.ForeignKey(OrderInfo)
    #商品价格
    price=models.DecimalField(max_digits=5,decimal_places=2)
    #商品数量
    count=models.IntegerField()
# Create your models here.
