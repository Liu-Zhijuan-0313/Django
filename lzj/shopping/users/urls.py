from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^userinfo/$', views.userinfo, name="userinfo"),
    # 验证码
    url(r'^create_code_img/$', views.create_code_img, name="create_code_img"),
    # 修改用户信息
    url(r'^userupdate/$', views.userupdate, name="userupdate"),
    # 修改用户头像
    url(r'^user_update_img/$', views.user_update_img, name="user_update_img"),
    # 修改用户密码
    url(r'^user_update_pwd/$', views.user_update_pwd, name="user_update_pwd"),
]