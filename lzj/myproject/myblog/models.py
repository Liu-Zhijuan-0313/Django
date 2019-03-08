from django.db import models

# Create your models here.
# 设置富文本编辑器模块
from tinymce.models import HTMLField


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    avater1 = models.ImageField(upload_to="static/img/", default="/static/myblog/img/头像.png")


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    # content = models.TextField()
    content = HTMLField()
    author = models.ForeignKey(Users)
