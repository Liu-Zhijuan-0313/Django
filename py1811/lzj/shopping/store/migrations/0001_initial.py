# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-16 02:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='店铺名称')),
                ('cover', models.ImageField(default='static/images/store/default.png', upload_to='static/images/store', verbose_name='店铺封面')),
                ('intro', models.TextField(verbose_name='店铺描述')),
                ('openTime', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, verbose_name='店铺状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='店铺所属用户')),
            ],
        ),
    ]
