from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
from django.shortcuts import redirect, reverse
# 验证码
from . import utills
from io import BytesIO


"验证码"
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


# 博客首页面
def index(request, n):
    user = models.Users.objects.get(name=n)
    return render(request, "myblog/index.html", {"user": user, "request": request})


# 注册
def register(request):
    if request.method == "GET":
        return render(request, "myblog/register.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        code = request.POST.get("code")
        if code == request.session['code']:
            try:
                user = models.Users(name=name, password=password)
                user.save()
                return render(request, "myblog/login.html")
            except:
                msg = "昵称已存在, 请重新注册"
                return render(request, "myblog/register.html", {"msg": msg})
        else:
            msg = "验证码错误，请重新注册"
            return render(request, "myblog/register.html", {"msg": msg})


# 登录

def login(request):
    if request.method == "GET":
        return render(request, "myblog/login.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        code = request.POST.get("code")
        # print(name, password)
        # 判断验证码，昵称，密码是否正确
        if code == request.session['code']:
            try:

                user = models.Users.objects.get(name=name, password=password)
                request.session["loginUser"] = user.name
                # print(request.session["loginUser"])
                return redirect(reverse("myblog:index", args=(name,)))
            except:
                msg = "昵称或密码错误，请重新登录"
                return render(request, "myblog/login.html", {"msg": msg})
        else:
            msg = "验证码错误，请重新登录"
            return render(request, "myblog/login.html", {"msg": msg})


# 查看用户信息, 登陆之后跳转到此页面
def userinfo(request):
    n = request.session["loginUser"]
    try:
        if request.method == "GET":
            user = models.Users.objects.get(name=n)
            print(user.avater1)
            return render(request, "myblog/userinfo.html", {"user": user})
        elif request.method == "POST":
            user = models.Users.objects.get(name=n)
            return redirect(reverse("myblog:userupdate"))
    except:
        return redirect(reverse("myblog:login"))


# 修改用户信息
def userupdate(request):
    n = request.session["loginUser"]
    if request.method == "GET":
        user = models.Users.objects.get(name=n)
        return render(request, "myblog/userupdate.html", {"user": user})
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        password = request.POST.get("password")
        avater1 = request.FILES.get("avater1")
        try:
            user = models.Users.objects.get(name=n)
            print(user.id)
            id = user.id
            user = models.Users(id=id, name=name, age=age, gender=gender, email=email, password=password, avater1=avater1)
            user.save()
            return redirect(reverse("myblog:userinfo"))
        except:
            msg = "此昵称已存在，请重新修改内容"
            user = models.Users.objects.get(name=n)
            return render(request, "myblog/userupdate.html", {"msg": msg, "user": user})


# 写文章
def artilewrite(request):
    n = request.session["loginUser"]
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
        try:
            article = models.Article(title=title, content=content, author=user)
            article.save()
            return redirect(reverse("myblog:articleread1",args=(article.title,)))
        except Exception as e:
            msg = "博客标题重复，请重新写内容"
            user = models.Users.objects.get(name=n)
            return render(request, "myblog/articlewrite.html", {"user": user, "msg": msg})


# 查看文章列表
def articlelist(request):
    if request.method == "GET":
        article = models.Article.objects.all()
        return render(request, "myblog/articlelist.html", {"article": article})


# 文章内容详情
def articleread1(request, a):
    if request.method == "GET":
        article = models.Article.objects.filter(title=a)
        return render(request, "myblog/articleread1.html", {"article": article})


"修改文章内容"


def articleupdate(request, a):
    article = models.Article.objects.get(title=a)
    if request.session["loginUser"] == article.author.name:
        if request.method == "GET":
            article = models.Article.objects.get(title=a)
            return render(request, "myblog/articleupdate.html", {"article": article})
        elif request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")
            author = request.POST.get("author")
            # print(title, content)

            user = models.Users.objects.get(name=author)
            article = models.Article(id=article.id, title=title, content=content, author_id=user.id)
            article.save()
            return redirect(reverse("myblog:articleread1", args=(article.title,)))
    else:
        msg = "不是作者本人，无法修改此文章"
        return render(request, "myblog/articledelete.html", {"msg": msg})


# 删除文章
def articledelete(request, a):
    article = models.Article.objects.get(title=a)
    if request.session["loginUser"] == article.author.name:

        article.delete()
        return redirect(reverse("myblog:articlelist"))
    else:
        msg = "不是作者本人，无法删除此文章"
        return render(request, "myblog/articledelete.html", {"msg": msg})


# 退出登录
def logout(request):
    try:
        del request.session["loginUser"]
        return redirect(reverse("myblog:login"))
    except Exception as f:
        return redirect(reverse("myblog:login"))
