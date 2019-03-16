from django.conf.urls import url


from . import views

urlpatterns = [
    # 商品添加
    url(r'^add/$', views.add, name="add"),
    url(r'^findTypeByPId/$', views.findTypeByPId, name="findTypeByPId"),
]