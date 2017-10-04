# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_goods', '0001_initial'),
        ('tt_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='tt_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='tt_user.UserInfo')),
            ],
        ),
    ]
