from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<count>\d+)/(?P<good_id>\w+)/add/$', views.add, name="add"),
    url(r'^list/$', views.list, name="list"),
    url(r'^(\w+)/delete/$', views.delete, name="delete"),
]