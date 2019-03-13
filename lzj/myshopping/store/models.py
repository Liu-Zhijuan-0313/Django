from django.db import models

# Create your models here.
from users.models import Users
from datetime import datetime
# 富文本编辑器
from tinymce.models import HTMLField
"""
店铺信息：Store
属性：
    店铺编号：id
    店铺名称：name
    店铺封面：cover
    店铺描述：intro
    开店时间：opener_time
    店铺状态：status 0 1 2 3 ……
    所属用户：users
"""


# 3.店铺信息
class Store(models.Model):
    # 店铺编号
    id = models.AutoField(primary_key=True)
    # 店铺名称
    name = models.CharField(max_length=255, unique=True)
    # 店铺封面
    cover = models.ImageField(upload_to="static/images/store", default="static/images/store/店铺封面.jpg")
    # 店铺描述
    # intro = models.TextField()
    intro = HTMLField()
    # 开店时间
    #  auto_now_add=True，字段在实例第一次保存的时候会保存当前时间，
    # 不管你在这里是否对其赋值。但是之后的save()是可以手动赋值的。
    # 也就是新实例化一个model，想手动存其他时间，就需要对该实例save()之后赋值然后再save()。
    opener_time = models.DateTimeField(auto_now_add=True)
    # 店铺状态 # 0 正常营业 1 暂停营业 2 永久删除
    status = models.IntegerField(default=0)
    # 所属用户
    # 创建多对一的关系的, 需要在Foreign的第二参数中加入on_delete = models.CASCADE
    # 主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
