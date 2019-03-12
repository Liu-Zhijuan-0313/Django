from django.db import models
from users.models import Users
# Create your models here.
"""
收货地址：
属性：
    地址编号         id
    所属用户         users
    收货人姓名       recv_name
    收货人联系方式   recv_phone
    国家             native
    省区             provice
    市区             city
    县区             country
    街道             street
    详细描述         desc
    是否默认地址     status[True默认 False非默认]
"""


# 2.收货地址
class Address(models.Model):
    # 地址编号
    id = models.AutoField(primary_key=True)
    # 所属用户
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # 收货人姓名
    recv_name = models.CharField(max_length=255)
    # 收货人联系方式
    recv_phone = models.CharField(max_length=255)
    # 国家
    native = models.CharField(max_length=255)
    # 省区
    provice = models.CharField(max_length=255)
    # 市区
    city = models.CharField(max_length=255)
    # 县区
    country = models.CharField(max_length=255)
    # 街道
    street = models.CharField(max_length=255)
    # 详细描述
    desc = models.CharField(max_length=255)
    # 是否默认地址
    status = models.BooleanField(default=False)
