from django.conf.urls import url


from . import views

urlpatterns = [
    # 商品添加
    # url(r'^add/$', views.add, name="add"),
    url(r'^(\d+)/add/$', views.add, name="add"),
    url(r'^findTypeByPId/$', views.findTypeByPId, name="findTypeByPId"),
    url(r'^(?P<g_id>\d+)/detail/$', views.detail, name="detail"),
    url(r'^list/$', views.list, name="list"),
]