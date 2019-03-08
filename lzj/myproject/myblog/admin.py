from django.contrib import admin

# Register your models here.
# 把 models中的类注册给后台管理平台
from . import models
admin.site.register(models.Users)
admin.site.register(models.Article)


