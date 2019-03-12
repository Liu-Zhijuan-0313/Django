from django.db import models

# Create your models here.
from users.models import Users
from goods.models import Goods
"""
购物车信息：Shopcart
属性：
    购物编号：id
    购买商品：goods
    购买数量：count
    添加时间：add_time
    小计金额：subtotal
    所属用户：users
"""


# 6.购物车
class Shopcart(models.Model):
    # 购物编号
    id = models.AutoField(primary_key=True)
    # 购买商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    # 购买数量
    count = models.IntegerField()
    # 添加时间
    add_time = models.DateTimeField(auto_now_add=True)
    # 小计金额
    subtotal = models.FloatField()
    # 所属用户
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

