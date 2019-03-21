"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 用户模块
    url(r'^users/', include("users.urls", namespace="users")),
    # 公共模块
    url(r'^', include("commons.urls", namespace="commons")),
    # 店铺模块
    url(r'^store/', include("store.urls")),
    # 商品模块
    url(r'^goods/', include("goods.urls", namespace="goods")),
    # 购物车
    url(r'^shopcart/', include("shopcart.urls", namespace="shopcart")),
    # 地址
    url(r'^address/', include("address.urls", namespace="address")),
    # 订单
    url(r'^orders/', include("orders.urls", namespace="orders")),
]