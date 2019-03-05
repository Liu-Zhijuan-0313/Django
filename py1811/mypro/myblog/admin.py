from django.contrib import admin
from . import models

# Register your models here.

# models中的类注册给后台管理平台
admin.site.register(models.User)
admin.site.register(models.Article)
admin.site.register(models.Article2)