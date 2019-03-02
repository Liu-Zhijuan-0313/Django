from django.conf.urls import url
from . import views
app_name = "myblog"

urlpatterns = [
    url(r'^(\w+)/index/$', views.index, name="index"),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login, name="login"),
    url(r'^(\w+)/userinfo/$', views.userinfo, name="userinfo"),
    url(r'^(\w+)/userupdate/$', views.userupdate, name="userupdate"),
    url(r'^(\w+)/articlewrite/$', views.artilewrite, name="articlewrite"),
    url(r'^articleread/$', views.articleread),
    url(r'^(\w+)/articleupdate/$', views.articleupdate, name="articleupdate")
]