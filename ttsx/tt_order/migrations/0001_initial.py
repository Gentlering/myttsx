# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0001_initial'),
        ('tt_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='tt_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('odate', models.DateTimeField(auto_now_add=True)),
                ('oIsPay', models.BooleanField(default=False)),
                ('ototal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='tt_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='tt_order.OrderInfo'),
        ),
    ]
