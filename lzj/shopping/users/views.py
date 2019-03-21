from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

# 1.验证码
from django.http import HttpResponse
from io import BytesIO
from . import utills


def create_code_img(request):
    # 在内存中开辟空间用以生成临时的图片
    b = BytesIO()
    img, code = utills.create_code()
    img.save(b, 'PNG')
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    # 方便拿过来用户的输入做验证
    request.session['code'] = code
    return HttpResponse(b.getvalue())


# dajngo默认有注册登录退出的装饰器
from django.contrib.auth import authenticate, logout, login

from . import models


# 2.登录
def user_login(request):
    if request.method == "GET":
        try:
            next_url = request.GET['next']
        except:
            next_url = "/"
        return render(request, "users/login1.html", {"next_url": next_url})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

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
                return  render(request, "users/login1.html", {"error_code": 2, "msg": "你的帐号已经被锁定,请联系管理员"})

        else:
            return render(request, "users/login1.html", {"error_code": 3, "msg": "你的用户名或者密码错误，请重新登录"})


# 验证码，密码，用户名，昵称
# 注册之后进入用户详情页面，自己绑定邮箱
# strip()可以去除两边的空格
# 3.注册
def register(request):
    if request.method == "GET":
        return render(request, "users/register1.html")
    elif request.method == "POST":

        username = request.POST.get("username")
        nickname = request.POST.get("nickname")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        # 密码是否重复
        if password != password1:
            return render(request, "users/register1.html", {"error_code": 1, "msg": "两次密码不一致，请重新输入"})
        # 判断用户名是否可用
        try:
            User.objects.get(username=username)
            return render(request, "users/register1.html", {"error_code": 2, "msg": "该用户已存在,请重新输入"})
        except:
            # 判断昵称不能重复
            try:
                user = models.Userinfo.objects.get(username=username)
                return render(request, "users/register1.html",  {"error_code": 3, "msg": "该用户昵称已存在,请重新输入"})
            except:
                # 保存用户信息
                user = User.objects.create_user(username=username, password=password)
                userinfo = models.Userinfo(nickname=nickname, user=user)
                user.save()
                userinfo.save()
                return render(request, "users/login1.html", {"error_code": 1, "msg": "用户注册成功,请登录"})


from django.contrib.auth.decorators import login_required
# 规定登录用户之后才访问
# 4.退出
@login_required
def user_logout(request):
    logout(request)
    return render(request, "users/login1.html", {"error_code": 4, "msg": "退出成功，请重新登录"})


@login_required
def userinfo(request):
    return render(request, "users/userinfo1.html")


# 5.修改用户信息
@login_required()
def userupdate(request):
    if request.method == "GET":
        return render(request, "users/userupdate1.html")
    elif request.method == "POST":

            username = request.POST.get("username")
            nickname = request.POST.get("nickname")
            age = request.POST.get("age")
            gender = request.POST.get("gender")
            phone = request.POST.get("phone")

            userinfo = models.Userinfo.objects.get(user=request.user)
            userinfo.nickname = nickname
            userinfo.age = age
            userinfo.gender = gender
            userinfo.phone = phone
            userinfo.save()

            user = request.user
            user.username = username
            user.save()
            # return HttpResponse("修改完成")
            return redirect(reverse("users:userinfo"))


# 6.修改用户头像
@login_required()
def user_update_img(request):
    if request.method == "GET":
        return render(request, "users/user_update_img2.html")
    elif request.method == "POST":
        header = request.FILES["header"]

        userinfo = models.Userinfo.objects.get(user=request.user)
        userinfo.header = header
        userinfo.save()

        # return HttpResponse("修改完成")
        return redirect(reverse("users:userinfo"))


# 加密解密
from django.contrib.auth.hashers import make_password, check_password

# 7.修改用户密码
@login_required()
def user_update_pwd(request):

    # 加密之后的数据库密码，判断原密码输入是否正确需要解密密码
    print(request.user.password)
    if request.method == "GET":
        return render(request, "users/user_update_pwd2.html")
    elif request.method == "POST":
        # userpass原密码，userpass01，userpass02新密码
        password = request.POST.get("password")
        userpass01 = request.POST.get("userpass01")
        userpass02 = request.POST.get("userpass02")

        if check_password(password, request.user.password) == False:
            msg = "原密码输入不正确"
            return render(request, "users/user_update_pwd2.html", {"msg": msg})
        elif check_password(password, request.user.password) == True:

            if userpass01 == userpass02:
                user = request.user
                user.password = make_password(userpass01)
                user.save()
                # return HttpResponse("修改完成")
                return redirect(reverse("users:userinfo"))
            elif userpass01 != userpass02:
                msg = "两次密码输入不一致"
                return render(request, "users/user_update_pwd2.html", {"msg": msg})

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
