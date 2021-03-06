# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-11 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('cover', models.ImageField(default='static/images/store/店铺封面.png', upload_to='static/images/store')),
                ('intro', models.TextField()),
                ('opener_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
    ]
