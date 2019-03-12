from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from . import models
from . import utills
# Create your views here.
from django.db.models import Q



def index(request):
    return render(request, "users/userupdate2.html")


# 验证码
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


# 注册
def register(request):
    if request.method == "GET":
        return render(request, "users/register1.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        userpass = request.POST.get("userpass")
        userpass1 = request.POST.get("userpass1")
        code = request.POST.get("code")
        if request.session['code'] == code:
            if userpass == userpass1:
                user = models.Users(username=username, phone=phone, email=email, userpass=userpass)
                user.save()
                # return HttpResponse("注册成功")
                return redirect(reverse("users:login"))
            elif userpass != userpass1:
                msg = "两次密码输入不一致，请重新注册"
                return render(request, "users/register1.html", {"msg": msg})
        else:
            msg = "验证码输入不正确，请重新注册"
            return render(request, "users/register1.html", {"msg": msg})


# 登录
def login(request):
    if request.method == "GET":
        return render(request, "users/login1.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("userpass")
        code = request.POST.get("code")
        if request.session['code'] == code:
            try:
                user = models.Users.objects.get(Q(username=username, userpass=userpass) | Q(email=username, userpass=userpass) | Q(phone=username, userpass=userpass))
                request.session['loginuser'] = user.username
                # return HttpResponse("登录成功")
                return redirect(reverse("users:userinfo"))
            except:
                return render(request, "users/login1.html")
        else:
            msg = "验证码输入不正确，请重新登录"
            return render(request, "users/login1.html", {"msg": msg})


# 查看用户信息
def userinfo(request):
    username = request.session['loginuser']
    if request.method == "GET":
        user = models.Users.objects.get(username=username)
        return render(request, "users/userinfo2.html", {"user": user})


# 修改用户信息
def userupdate(request):
    username1 = request.session['loginuser']
    user = models.Users.objects.get(username=username1)
    if request.method == "GET":
        return render(request, "users/userupdate2.html", {"user": user})
    elif request.method == "POST":
            username = request.POST.get("username")
            userpass = request.POST.get("userpass")
            nickname = request.POST.get("nickname")
            age = request.POST.get("age")
            gender = request.POST.get("gender")
            phone = request.POST.get("phone")
            email = request.POST.get("email")

            user = models.Users(id=user.id, regist_time=user.regist_time, username=username, userpass=userpass, nickname=nickname, age=age, gender=gender, phone=phone, email=email)
            user.save()
            # return HttpResponse("修改完成")
            return redirect(reverse("users:userinfo"))



