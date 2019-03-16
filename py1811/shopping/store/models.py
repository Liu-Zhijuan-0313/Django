from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# upload_to不能传绝对路径
# auto_now_add=True：第一次开店时间，后期不变
# auto_now=True：以后每次修改都会更新时间
# on_delete=models.CASCADE：级联删除，删除用户的时候店铺也删除
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="店铺名称")
    cover = models.ImageField(upload_to="static/images/store", default="static/images/store/default.png", verbose_name="店铺封面")
    intro = models.TextField(verbose_name="店铺描述")
    openTime = models.DateTimeField(auto_now_add=True)
    # 0正常营业，1暂停营业，2永久删除
    status = models.IntegerField(default=0, verbose_name="店铺状态")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店铺所属用户")

