from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# username用户名
# verbose_name注解，后台显示
class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255, verbose_name="用户昵称")
    age = models.IntegerField(default=18, verbose_name="用户年龄")
    gender = models.CharField(max_length=10, default="男", verbose_name="性别")
    header = models.ImageField(upload_to="static/images/headers", default="static/images/headers/default.png", verbose_name="用户头像")
    phone = models.CharField(max_length=50, default=110, verbose_name="用户电话号码")
    # 和系统内置的用户管理一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE)
