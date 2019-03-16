from django.db import models
from store.models import Store


# Create your models here.
# 商品类型
class GoodsType(models.Model):
    id = models.AutoField(primary_key=True)
    gt_name = models.CharField(max_length=255, unique=True, verbose_name="商品类型名称")
    cover = models.ImageField(upload_to="static/images/goods", default="static/images/goods/default.png", verbose_name="商品图片")
    gt_desc = models.TextField(verbose_name="商品类别描述")
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name="父级类型", on_delete=models.CASCADE)


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="商品名称")
    price = models.FloatField(verbose_name="单价")
    stock = models.IntegerField(verbose_name="库存")
    count = models.IntegerField(default=0, verbose_name="销量")
    creatTime = models.DateTimeField(auto_now_add=True)
    intro = models.TextField()
    stores = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="商品所属商店")
    goodstype = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name="商品类型")


class GoodsImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to="static/images/goods", default="static/images/goods/default.png", verbose_name="商品图片")
    intro = models.TextField(verbose_name="商品图片描述", null=True)
    status = models.BooleanField(default=False, verbose_name="是否默认显示该图片")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="所属商品")
