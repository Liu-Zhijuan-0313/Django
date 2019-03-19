from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^address_add/$', views.address_add, name="address_add"),
    url(r'^address_list/$', views.address_list, name="address_list")

]