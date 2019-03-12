from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    # 添加店铺
    url(r'^store_add/$', views.store_add, name="store_add")
]