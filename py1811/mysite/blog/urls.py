from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^register/$', views.register),
    url(r'^register1/$', views.register1),
    url(r'^login/$', views.login),
]