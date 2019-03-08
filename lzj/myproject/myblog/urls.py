from django.conf.urls import url
from . import views
app_name = "myblog"

urlpatterns = [
    url(r'^(\w+)/index/$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^userinfo/$', views.userinfo, name="userinfo"),
    url(r'^userupdate/$', views.userupdate, name="userupdate"),
    url(r'^articlewrite/$', views.artilewrite, name="articlewrite"),
    url(r'^articlelist/$', views.articlelist, name="articlelist"),
    url(r'^(\w+)/articleupdate/$', views.articleupdate, name="articleupdate"),
    # "验证码"
    url(r'^create_code_img/$', views.create_code_img, name="create_code_img"),
    url(r'^(\w+)/articleread1/$', views.articleread1, name="articleread1"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^(\w+)/articledelete/$', views.articledelete, name="articledelete"),
]