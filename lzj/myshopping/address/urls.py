from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    # 添加地址
    url(r'^address_add/$', views.address_add, name="address_add"),
    # 查看所有地址
    url(r'^address_readlist/$', views.address_readlist, name="address_readlist"),
    # 查看地址详情
    url(r'^(\w+)/address_read/$', views.address_read, name="address_read"),
    # 删除地址
    url(r'^(\w+)/address_delete/$', views.address_delete, name="address_delete"),
    # 修改地址
    url(r'^(\w+)/address_update/$', views.address_update, name="address_update")
]