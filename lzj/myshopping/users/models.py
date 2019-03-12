from django.db import models
from datetime import datetime
# Create your models here.

"""
用户类型：Users
属性：
    用户编号    id
    登录账号    username
    登录密码    userpass
    用户昵称    nickname
    用户年龄    age
    用户性别    gender
    用户头像    header
    联系方式    phone
    电子邮箱    email
    注册时间    regist_time
    上次登录时间   last_login_time
   
"""


# 1.用户类型
class Users(models.Model):
    # 用户编号
    id = models.AutoField(primary_key=True)
    # 登录账号
    username = models.CharField(max_length=255, unique=True)
    # 登录密码
    userpass = models.CharField(max_length=255)
    # 用户昵称
    nickname = models.CharField(max_length=255)
    # 用户年龄
    age = models.IntegerField(default=18)
    # 用户性别
    gender = models.CharField(max_length=255)
    # 用户头像
    header = models.ImageField(upload_to="static/images/headers",  default="static/images/headers/默认头像.png")
    # 联系方式
    phone = models.CharField(max_length=255)
    # 电子邮箱
    email = models.EmailField()
    # 注册时间
    regist_time = models.DateTimeField(auto_now_add=True)
    # 上次登录时间
    last_login_time = models.DateTimeField(auto_now=True)
