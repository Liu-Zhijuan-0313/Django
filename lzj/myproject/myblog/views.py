from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
from django.shortcuts import redirect, reverse


def index(request, n):
    user = models.Users.objects.get(name=n)
    return render(request, "myblog/index.html", {"user": user})


# 注册
def register(request):
    if request.method == "GET":
        return render(request, "myblog/register.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        try:
            user = models.Users(name=name, password=password)
            user.save()
            return render(request, "myblog/login.html")
        except:
            msg = "昵称已存在, 请重新注册"
            return render(request, "myblog/register.html", {"msg": msg})


# 登录
def login(request):
    if request.method == "GET":
        return render(request, "myblog/login.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        print(name, password)
        try:
            print(type(name), password)
            models.Users.objects.get(name=name, password=password)
            return redirect(reverse("myblog:index", args=(name,)))
        except:
            msg = "昵称或密码错误，请重新登录"
            return render(request, "myblog/login.html", {"msg": msg})


# 查看用户信息, 登陆之后跳转到此页面
def userinfo(request, n):
    if request.method == "GET":
        user = models.Users.objects.get(name=n)
        return render(request, "myblog/userinfo.html", {"user": user})


# 修改用户信息
def userupdate(request, n):
    if request.method == "GET":
        user = models.Users.objects.get(name=n)
        return render(request, "myblog/userupdate.html", {"user": user})
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = models.Users.objects.get(name=n)
            print(user.id)
            id = user.id
            user = models.Users(id=id, name=name, age=age, gender=gender, email=email, password=password)
            user.save()
            return redirect(reverse("myblog:userinfo", args=(n,)))
        except:
            msg = "此昵称已存在，请重新修改内容"
            user = models.Users.objects.get(name=n)
            return render(request, "myblog/userupdate.html", {"msg": msg, "user": user})


# 写文章
def artilewrite(request, n):
    if request.method == "GET":

        user = models.Users.objects.get(name=n)
        # article = models.Article(title="标题", content="文章内容", author=user)
        # article.save()
        return render(request, "myblog/articlewrite.html", {"user": user})
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = models.Users.objects.get(name=n)

        # 作者外键是个User用户对象
        article = models.Article(title=title, content=content, author=user)
        article.save()
        return HttpResponse("文章写作完毕")


# 查看文章
def articleread(request):
    if request.method == "GET":
        user = models.Article.objects.all()
        return render(request, "myblog/articleread.html", {"article": user})


# 修改文章内容
def articleupdate(request, n):
    if request.method == "GET":
        user = models.Users.objects.get(name=n)
        article = models.Article.objects.all()
        return render(request, "myblog/articleupdate.html", {"article": article})
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title, content)
        user = models.Users.objects.get(name=n)
        id = user.id
        article = models.Article(id=id, title=title, content=content, author=user)
        article.save()
        return HttpResponse("文章修改完成")

