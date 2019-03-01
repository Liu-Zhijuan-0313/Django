from django.conf.urls import url
from . import views


# 子路径
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^(\d+)/list/$', views.list),
    url(r'^(?P<name>\w+)/list2/$', views.list2),
    url(r'^list3/$', views.list3),
    url(r'^list4/$', views.list4),
    url(r'^list5/$', views.list5),
    url(r'^list6/$', views.list6),
]