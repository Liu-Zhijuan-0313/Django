from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^address_add/$', views.address_add, name="address_add"),
    url(r'^address_list/$', views.address_list, name="address_list"),
    # 查看地址详情
    url(r'^(\w+)/address_read/$', views.address_read, name="address_read"),
    # 删除地址
    url(r'^(\w+)/address_delete/$', views.address_delete, name="address_delete"),
    # 修改地址
    url(r'^(\w+)/address_update/$', views.address_update, name="address_update"),

]