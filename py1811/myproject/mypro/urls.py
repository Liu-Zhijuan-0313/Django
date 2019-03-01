"""mypro URL Configuration

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
# 子模块路由导入到根模块
from django.conf.urls import include
from django.contrib import admin
from . import views
# regex正则表达式, view视图, kwargs=None, name=None
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r"^findall/$", views.findall),
    url(r"^allgood/$", views.allgood),
    url(r"^delete/$", views.delete),
    url(r'^myblog/', include('myblog.urls')),
]
