from django.db import models
from tt_user.models import UserInfo

class CartInfo(models.Model):
    user=models.ForeignKey(UserInfo)
    goods=models.ForeignKey('tt_goods.GoodsInfo')
    count=models.IntegerField()
# Create your models here.
