from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^login/$", views.user_login, name="user_login"),
    url(r"^userinfo/$", views.userinfo, name="userinfo"),
    url(r"^register/$", views.register, name="register"),
    url(r"^logout/$", views.user_logout, name="user_logout"),
    url(r"^add_address/$", views.add_address, name="add_address"),
    url(r"^address_list/$", views.address_list, name="address_list"),
]