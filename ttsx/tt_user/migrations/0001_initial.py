# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('uaddress', models.CharField(max_length=100)),
                ('uphone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('isValid', models.BooleanField(default=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='useraddressinfo',
            name='user',
            field=models.ForeignKey(to='tt_user.UserInfo'),
        ),
    ]
