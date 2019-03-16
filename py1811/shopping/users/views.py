from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User


# dajngo默认有注册登录退出的装饰器
from django.contrib.auth import authenticate, logout, login
# Create your views here.
from . import models


def user_login(request):
    if request.method == "GET":
        try:
            next_url = request.GET['next']
        except:
            next_url = "/"
        return render(request, "users/login.html", {"next_url": next_url})
    elif request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()

        # 如果为空，加/,跳转到首页面
        next_url = request.POST.get("next", "/")

        #  If the given credentials are valid, return a User object.
        # 如果验证通过，返回用户对象
        # 等价于User.objects.filter(username=username, password=password).fister()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # request.session也取不到
                # 将验证通过的用户信息保存在request, request.user.nickname
                login(request, user)
                return redirect(next_url)
                # return render(request, "users/userinfo.html", {"user": user})
            else:
                return  render(request, "users/login.html", {"error_code": 2, "msg": "你的帐号已经被锁定,请联系管理员"})

        else:
            return render(request, "users/login.html", {"error_code": 3, "msg": "你的用户名或者密码错误，请重新登录"})


# 验证码，密码，用户名，昵称
# 注册之后进入用户详情页面，自己绑定邮箱
# strip()可以去除两边的空格
def register(request):
    if request.method == "GET":
        return render(request, "users/register.html")
    elif request.method == "POST":

        username = request.POST.get("username").strip()
        nickname = request.POST.get("nickname").strip()
        password = request.POST.get("password").strip()
        password1 = request.POST.get("password1").strip()

        # 密码是否重复
        if password != password1:
            return render(request, "users/register.html", {"error_code": 1, "msg": "两次密码不一致，请重新输入"})
        # 判断用户名是否可用
        try:
            User.objects.get(username=username)
            return render(request, "users/register.html", {"error_code": 2, "msg": "该用户已存在,请重新输入"})
        except:
            # 判断昵称不能重复
            try:
                user = models.Userinfo.objects.get(username=username)
                return render(request, "users/register.html",  {"error_code": 3, "msg": "该用户昵称已存在,请重新输入"})
            except:
                # 保存用户信息
                user = User.objects.create_user(username=username, password=password)
                userinfo = models.Userinfo(nickname=nickname, user=user)
                user.save()
                userinfo.save()
                return render(request, "users/login.html", {"error_code": 1, "msg": "用户注册成功,请登录"})


from django.contrib.auth.decorators import login_required
# 规定登录用户之后才访问
@login_required
def user_logout(request):
    logout(request)
    return render(request, "users/login.html", {"error_code": 4, "msg": "退出成功，请重新登录"})


@login_required
def userinfo(request):
    return render(request, "users/userinfo.html")

# ==================================================================


"""
users模块：
    登录，注册，退出，
    用户详情，
    密码修改，修改头像，修改其他属性，
    查询其他用户的空间
    验证码，加密放到公共模块
    用户的增删改查，有超级管理员管理，交给后台
公共模块：(项目的公共部分，如首页面数据展示，如公共的工具类)
    项目首页面
    验证码，加密
    工具类
    ......
    数据字典：短而精湛的数据
"""
