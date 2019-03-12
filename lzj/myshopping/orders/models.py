from django.db import models

# Create your models here.
from users.models import Users
"""
订单：Order
属性：
    订单编号：id
    下单时间：order_time
    所属用户：users
    收货人：recv_name
    收货地址：recv_address 非外键
    联系方式：recv_phone
    备注信息：recv_remark
    总计金额：totale
"""


# 7.订单
class Order(models.Model):
    # 订单编号
    id = models.AutoField(primary_key=True)
    # 下单时间
    order_time = models.DateTimeField(auto_now_add=True)
    # 所属用户
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # 收货人
    recv_name = models.CharField(max_length=255)
    # 收货地址：
    recv_address = models.CharField(max_length=255)
    # 联系方式
    recv_phone = models.CharField(max_length=255)
    # 备注信息
    recv_remark = models.CharField(max_length=255)
    # 总计金额
    totable = models.FloatField()


"""
订单单项：OrderItem
属性：
    项目编号：id
    购买商品编号：oi_goods_id
    购买商品名称：oi_goods_name
    购买商品单价：oi_goods_price
    购买商品数量：oi_goods_count
    成交价格：deal_price
    所属订单：order
"""


# 8.订单单项
class OrderItem(models.Model):
    # 项目编号
    id = models.AutoField(primary_key=True)
    # 购买商品编号
    oi_goods_id = models.CharField(max_length=255)
    # 购买商品名称
    oi_goods_name = models.CharField(max_length=255)
    # 购买商品单价
    oi_goods_price = models.FloatField()
    # 购买商品数量
    oi_goods_count = models.IntegerField()
    # 成交价格,总价
    deal_price = models.FloatField()
    # 所属订单
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
