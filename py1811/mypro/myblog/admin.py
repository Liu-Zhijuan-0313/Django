from django.contrib import admin
from . import models

# Register your models here.

# models中的类注册给后台管理平台


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


# 注册第二种方法：加装饰器
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    # # 1.指定展示列表
    list_display = ['name', 'age']
    # 2.过滤器:指定过滤条件
    list_filter = ['age', 'name']
    # 3.指定分页数量
    list_per_page = 3
    # 4.增加用户的时候显示的属性，
    # 和修改用户信息的时候显示的属性,
    fields = ['name', 'age']

    # 5.选中前面的选框，可以做一些动作
    actions_on_bottom = True
    actions_on_top = False
    # 6.设置搜索的选项
    search_fields = ['name', 'age']
    # 7.ordering设置默认排序字段,
    # 负号表示降序，
    # 先按照年龄降序，如果年龄相同的再按照名字降序
    ordering = ('-age', '-name')

    # 8.设置成链接，点进去可进行编辑
    # list_display_links = ['name', 'age']

    # 9.不用点进去，可直接编辑内容
    # list_display_links和list_editable用一个即可，有冲突
    list_editable = ['age']


# 注册第一种方法
# admin.site.register(models.User, UserAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Article2, ArticleAdmin)