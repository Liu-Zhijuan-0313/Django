from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    # 验证码
    url(r'^create_code_img/$', views.create_code_img, name="create_code_img"),
    # 注册
    url(r'^register/$', views.register, name="register"),
    # 登录
    url(r'^login/$', views.login, name="login"),
    # 查看用户信息
    url(r'^userinfo/$', views.userinfo, name="userinfo"),
    # 修改用户信息
    url(r'^userupdate/$', views.userupdate, name="userupdate"),
]
