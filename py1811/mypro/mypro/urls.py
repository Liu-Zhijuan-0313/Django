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
    # 子模块
    url(r'^myblog/', include('myblog.urls')),
    # 静态资源
    url(r'^index1/$', views.index1),
    # 主页面的路由
    url(r'^base/$', views.base),
    # 继承主页面的子页面路由
    url(r'^base_index1/$', views.base_index1),
]
