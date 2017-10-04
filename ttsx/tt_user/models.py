#coding=utf-8
from django.db import models
#用户的类
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemail=models.CharField(max_length=30)
    isValid=models.BooleanField(default=True)
    isActive=models.BooleanField(default=False)


#用户地址的类
class UserAddressInfo(models.Model):
    uname=models.CharField(max_length=20)
    uaddress=models.CharField(max_length=100)
    uphone=models.CharField(max_length=11)
    user=models.ForeignKey('UserInfo')
# Create your models here.
