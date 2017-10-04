# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('atitle', models.CharField(max_length=30, verbose_name='名称')),
                ('aParent', models.ForeignKey(null=True, blank=True, to='tt_user.AreaInfo', verbose_name='父级')),
            ],
        ),
    ]
