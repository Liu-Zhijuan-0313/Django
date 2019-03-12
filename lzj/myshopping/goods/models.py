from django.db import models

# Create your models here.
from store.models import Store


"""
商品类型：GoodsType
属性
    类型主键：id
    类型名称：gt_name
    图片：cover
    类型描述：gt_desc
    父级类型： null 自关联 注意一级类型应该允许为空
"""


# 商品类型
class GoodsType(models.Model):
    # 类型主键
    id = models.AutoField(primary_key=True)
    #  类型名称
    gt_name = models.CharField(max_length=255, unique=True)
    # 图片
    cover = models.ImageField()
    # 类型描述
    gt_desc = models.TextField()
    # 父级类型
    # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，即在Null字段显示为YES。
    # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    parent = models.ForeignKey('self', null=True, blank=True)


"""
商品信息：Goods
属性：
    商品编号：id
    商品名称：name
    商品单价：price
    商品库存：stock
    销售数量：count
    上架时间  add_time
    商品介绍：desc
    商品类型：goods_detail_type
    所属店铺：goods_store
"""


# 4.商品信息
class Goods(models.Model):
    # 商品编号
    id = models.AutoField(primary_key=True)
    # 商品名称
    name = models.CharField(max_length=255)
    # 商品单价
    price = models.FloatField()
    # 商品库存
    stock = models.IntegerField()
    # 销售数量
    count = models.IntegerField(default=0)
    # 上架时间
    add_time = models.DateTimeField(auto_now_add=True)
    # 商品介绍
    desc = models.TextField()
    # 商品类型
    goods_detail_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE)
    # 所属店铺
    goods_store = models.ForeignKey(Store, on_delete=models.CASCADE)


"""
商品图片：GoodsImage
属性：
    图片编号：id
    图片路径：path
    默认展示：status [True默认展示的商品图片]
    所属商品：goods
"""


# 5.商品图片
class GoodsImage(models.Model):
    # 图片编号
    id = models.AutoField(primary_key=True)
    # 图片路径
    path = models.ImageField(upload_to="static/images/goods", default="static/images/goods/商品图片.jpg")
    # 是否默认显示该图片
    status = models.BooleanField(default=True)
    # 商品图片描述
    intro = models.TextField(null=True, blank=True)
    # 所属商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)



