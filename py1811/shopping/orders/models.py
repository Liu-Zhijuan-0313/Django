from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订单所属用户")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="订单时间")
    recv_name = models.CharField(max_length=100, verbose_name="收件人")
    recv_tel = models.CharField(max_length=50, verbose_name="收件人电话")
    recv_address = models.CharField(max_length=255, verbose_name="收件人地址")
    # a商品加b商品。。。。
    all_price = models.FloatField(verbose_name="订单总金额")
    remark = models.CharField(max_length=255, verbose_name="订单备注")


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    good_id = models.IntegerField(verbose_name="订单编号")
    # 不上传图片，只是复制图片路径
    # 不能有外键
    goods_img = models.CharField(max_length=255, verbose_name="商品图片")
    goods_name = models.CharField(max_length=255, verbose_name="商品名称")
    goods_price = models.FloatField(max_length=255, verbose_name="商品价格")
    goods_count = models.FloatField(max_length=255, verbose_name="商品数量")
    goods_price_all = models.FloatField(max_length=255, verbose_name="商品总价")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

