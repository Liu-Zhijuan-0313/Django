# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-15 11:47
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
            name='Userinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=255, verbose_name='用户昵称')),
                ('age', models.IntegerField(default=18, verbose_name='用户年龄')),
                ('gender', models.CharField(default='男', max_length=10, verbose_name='性别')),
                ('header', models.ImageField(default='static/images/headers/default.png', upload_to='static/images/headers', verbose_name='用户头像')),
                ('phone', models.CharField(max_length=50, verbose_name='用户电话号码')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
