"""myshopping URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 用户
    url(r'^users/', include("users.urls", namespace="users")),
    # 地址
    url(r'^address/', include("address.urls", namespace="address")),
    # 店铺
    url(r'^store/', include("store.urls", namespace="store")),
    # 首页面
    url(r'^$', views.index),
    # 基本模块
    url(r'^base/$', views.base),
]
