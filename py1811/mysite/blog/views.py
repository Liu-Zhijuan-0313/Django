from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models


# def user(req):
#     return HttpResponse("lzj的用户信息")


def index(req):
    # us = models.User.create(name="bbb0", )
    # 第二种
    # us = models.User(name="lzj", age=22)
    # us.save()
    # 第三种
    # models.User.um.createuser(name="aaa", age=10)
    # 从数据库获取数据
    # user = models.Userregister.objects.get(id=22)
    # print(user.name)
    return HttpResponse("保存lzj的用户信息")


# ==========================================================
def register1(request):
    ur = models.Userregister(name="lzj", email="1602176692@qq.com", password="123456")
    ur.save()
    return HttpResponse("注册")


from django.shortcuts import loader
from django.shortcuts import render


# 注册
def register(request):
    if request.method == "GET":
        return render(request, "blog/register.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(name, email, password)
        user = models.Userregister(name=name, email=email, password=password)
        user.save()
        return HttpResponse("注册成功")


# 登录
def login(request):
    return render(request, "blog/login.html")



