from django.conf.urls import url
from . import views
urlpatterns = [
    # 确定订单
    url(r'^confirm/$', views.confirm, name="confirm"),
    # 支付
    url(r'^pay/$', views.pay, name="pay"),
    # 生成订单
    url(r'^done/$', views.done, name="done"),
    # 查看订单
    url(r'^list/$', views.list, name="list"),
    # 订单详情
    url(r'^(?P<o_id>\d+)/detail/$', views.detail, name="detail"),
    # 删除订单
    url(r'^(\w+)/delete/$', views.delete, name="delete")
]