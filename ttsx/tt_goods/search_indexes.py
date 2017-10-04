#! /usr/bin/env python3
# -*- coding:utf-8 -*-
#coding=utf-8
from haystack import indexes
from .models import GoodsInfo
#指定对于某个类的某些数据建立索引
class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    #由文本文件指定要查询的字段
    text = indexes.CharField(document=True, use_template=True)
    #指定要查询的表
    def get_model(self):
        return GoodsInfo
    #指定查询的行
    def index_queryset(self, using=None):
        return self.get_model().objects.all()