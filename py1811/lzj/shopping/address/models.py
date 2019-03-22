from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    recv_name = models.CharField(max_length=100, verbose_name="收货人")
    recv_tel = models.CharField(max_length=20, verbose_name="收货人的电话号码")
    province = models.CharField(max_length=100, verbose_name="收货人的省份")
    city = models.CharField(max_length=100, verbose_name="收货人的城市")
    area = models.CharField(max_length=100, verbose_name="收货人的县区")
    street = models.CharField(max_length=255, verbose_name="收货人的街道")
    desc = models.CharField(max_length=255, verbose_name="详细地址")
    is_default = models.BooleanField(default=False, verbose_name="是否是默认地址")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="地址的所属用户")
