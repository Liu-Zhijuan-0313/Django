from django.conf.urls import url
from . import views

app_name = "myblog"
# 子路径
urlpatterns = [

    # 三种方法：当刷新页面的会保存数据到数据库
    url(r'^index/$', views.index, name="index"),
    # 位置参数（路径URL中？后面的参数）
    url(r'^(\d+)/list/$', views.list),
    # "命名参数（路径URL中？后面的参数）"
    url(r'^(?P<name>\w+)/list2/$', views.list2),


    # 函数中的第一个参数request,请求对象
    url(r'^list3/$', views.list3),
    # 响应对象HttpResponse
    url(r'^list4/$', views.list4),


    # 第一种方法：响应模板
    url(r'^list5/$', views.list5),
    # 第二种方法：响应模板
    url(r'^list6/$', views.list6),


    # 注册
    url(r'^register/$', views.register, name="register"),
    # 登陆
    url(r'^login/$', views.login, name="login"),


    # 从数据库获取到数据，然后渲染到HTML页面，展示给用户
    url(r'^(\d+)/list7/$', views.list7, name="list7"),
    # "有参数和无参数，两种重定向"
    url(r'^list8/$', views.list8),

    url(r'^addarticle/$', views.addarticle, name="addarticle"),
    url(r'^create_code_img/$', views.create_code_img, name="create_code_img"),

    url(r'^jsontest/$', views.jsontest),
    url(r'^huihua/$', views.huihua),
]