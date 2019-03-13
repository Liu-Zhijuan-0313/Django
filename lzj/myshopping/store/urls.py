from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    # 1.添加店铺
    url(r'^store_add/$', views.store_add, name="store_add"),
    # 2.所有店铺列表
    url(r'^store_list/$', views.store_list, name="store_list"),
    # 3.店铺详情
    url(r'^(\w+)/store_detail/$', views.store_detail, name="store_detail"),
    # 4.修改店铺
    url(r'^(\w+)/store_update/$', views.store_update, name="store_update"),
    # 5.删除店铺
    url(r'^(\w+)/store_delete/$', views.store_delete, name="store_delete"),
    # 6.修改店铺封面
    url(r'^(\w+)/store_update_img/$', views.store_update_img, name="store_update_img"),
]