from django.http import HttpResponse
from . import models


"三种方法：当刷新页面的会保存数据到数据库"


def index(req):
    print(req.session.get("code"))
    # 第一种方法：调用模型类方法，构建对象
    # au = models.User.create(name='lzj', age=20)
    # 第二种方法：类属性的方式
    # au = models.User(name='aaa', age=21)
    # 调用对象的保存方法，保存数据到数据库
    # au.save()
    # 第三种方法：管理器
    # models.User.um.createUser(name='bbb', age=22)
    return HttpResponse("保存数据到数据库")
# ==========================================================


# 位置参数（路径URL中？后面的参数）
def list(request, age):
    print(age)
    return HttpResponse("路由里携带参数")


# 命名参数（路径URL中？后面的参数）
def list2(request, name):
    print(name)
    return HttpResponse("路由里携带‘命名’参数")


"""
# 函数中的第一个参数request
# path：路径
# method：请求方法
# GET：表示URL?后面的内容，以字典存储数据
# GET['aa']或者GET('aa')：获取字典里建对应的值
"""


def list3(request):
    print(request)
    # print(dir(request))
    print(request.path)
    print(request.method)
    print(request.GET)
    # print(request.GET['aa'], request.GET('bb'))
    return HttpResponse('第一个参数request')


# 响应对象HttpResponse
def list4(request):
    print(HttpResponse)
    print(dir(HttpResponse))
    print(HttpResponse.content)
    print(HttpResponse.charset)
    print(HttpResponse.status_code)
    return HttpResponse("<h1>响应对象</h1>")
# ============================================================


# 第一种方法：响应模板
from django.template import loader


def list5(request):
    temp = loader.get_template('myblog/index1.html')
    return HttpResponse(temp.render({'name': 'lzj'}, request))


# 第二种方法：响应模板
from django.shortcuts import render


def list6(request):
    # return render(request, 'myblog/index1.html')
    # 带参数
    return render(request, 'myblog/index1.html', {'name': 'lzj'})

# ===========================0301===========================================


# 注册
# def register(request):
#     if request.method == "GET":
#         return render(request, "myblog/register.html")
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         print(name, age)
#         user = models.User(name=name, age=age)
#         user.save()
#         return HttpResponse("注册成功")


# 后台数据库有这个用户则登录成功，没有则重新登录
# csrf_token跨站台请求伪造，
# 加了装饰器,html页面中{% csrf_token %}可不用写了
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "myblog/login.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        try:
            models.User.um.get(name=name, age=age)
            user = models.User.um.get(id=7)
            print(user.name)
            return HttpResponse("登录成功")
            # return render(request, "index1.html")

        except Exception as e:
            return render(request, "myblog/login.html")


# 从数据库获取到数据，然后渲染到HTML页面，展示给用户
def list7(request, id):
    user = models.User.um.get(id=7)
    users = models.User.um.all()
    print(user)
    print(id)
    return render(request, "myblog/index1.html", {"user": user, "users": users})

"""

转发和重定向比较：
转发：是一次请求,地址栏不变
重定向：是两次请求,地址栏发生变化

重定向好处：就是可以打向另外一个视图函数做对应的数据准备及相应的处理
重定向注意：如果携带参数，被重定向到的视图函数要提供形参接收，而且url配置的时候要
准备一个位置来携带这个参数。
"""
# 重定向的导入模块:
from django.shortcuts import redirect, reverse


"重定向，无参数"
# def list8(request):
#     print("gagnkj")
#     return redirect(reverse('myblog:login'))

"""
重定向：
有参数，则list7必须写个形式参数去接受，
list7的路由必须匹配这个形式参数
"""


def list8(request):
    print("gagnkj")
    return redirect(reverse('myblog:list7', args=(1,)))


# ========================第二周0304=============================

# 发表文章和富文本编辑器
def addarticle(request):
    if request.method == "GET":
        return render(request, "myblog/addarticle.html")
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        user = models.User.um.get(id=7)
        article = models.Article(title=title, content=content, author=user)
        article.save()
        return redirect(reverse("myblog:index"))

# 验证码
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


# AJAX
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def jsontest(request):
    u = models.User.um.get(id=7)
    u = model_to_dict(u)
    return JsonResponse(u)

# =======================0305===================================

"事务的流程"
# 1.导入库模块
from django.db import transaction
# 2.确保整个方法具有原子性
# @transaction.atomic
# def register(request):
#     if request.method == "GET":
#         return render(request, "myblog/register.html")
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         print(name, age)
#
#         # 3.在逻辑前设置还原点
#         s_id = transaction.savepoint()
#         try:
#             # 1 / 0
#             user = models.User(name=name, age=age)
#             user.save()
#             # 4.逻辑完全成立，提交事务
#             transaction.savepoint_commit(s_id)
#             return HttpResponse("注册成功")
#         except:
#             # 5.逻辑不完全成立，回滚事务
#             transaction.savepoint_rollback(s_id)
#             return HttpResponse("注册失败")


"form表单"
# from . import forms
# def register(request):
#     if request.method == "GET":
#         # 1.创建form类的实例
#         userform = forms.UserForm()
#         return render(request, "myblog/register.html", {"userform": userform})
#     elif request.method == "POST":
#         # 2.获取form提交的数据内容
#         form = forms.UserForm(request.POST)
#         print(form.data['name'])
#         # 2.下面方法也可以获取到请求内容，然后存入数据库
#         # name = request.POST.get("name")
#         # age = request.POST.get("age")
#         # print(name, age)
#         try:
#             # user = models.User(name=name, age=age)
#             user = models.User(name=form.data['name'], age=form.data['age'])
#             user.save()
#             return HttpResponse("注册成功")
#         except:
#             return HttpResponse("注册失败")


"第一种方法：普通字段CharField上传图片文件"
# def register(request):
#     if request.method == "GET":
#         return render(request, "myblog/register.html")
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#
#         # 1.获取文件
#         avater = request.FILES["avater"]
#         # 2.拼接上传路径
#         path = "static/img/" + avater.name
#         # 3.以流的方式打开上传
#         with open(path, "wb") as f:
#             # 4.分片写入
#             for file in avater.chunks():
#                 f.write(file)
#
#         print(name, age, path)
#         try:
#             user = models.User(name=name, age=age, avater=path)
#             user.save()
#             return HttpResponse("注册成功")
#         except:
#             return HttpResponse("注册失败")


"第二种方法：ImageField上传图片文件"
def register(request):
    if request.method == "GET":
        return render(request, "myblog/register.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        # 1.获取文件
        avater = request.FILES["avater"]
        print(name, age, avater)
        try:
            # 2.直接保存图片数据
            user = models.User(name=name, age=age, avater1=avater)
            user.save()
            return HttpResponse("注册成功")
        except:
            return HttpResponse("注册失败")


"会话跟踪"
def huihua(req):
    # 登录之后，登录的验证码可以会话跟踪
    print(req.session.get("code"))
    return HttpResponse("保存数据到数据库")

# =================0306===============================


"缓存取数据，没有从数据库取数据，并且存入缓存中"
from django.core.cache import cache


def redis1(request):
    print("从缓存中拿数据")
    us = cache.get("users")
    if us is None:
        print("从数据库取数据")
        users = models.User.um.all()
        print("存入缓存中")
        cache.set("users", users)
        print(cache.get("users"))
    return HttpResponse("从缓存取数据，没有从数据库取数据，并且存入缓存中")


"分页"
from django.core.paginator import Paginator, Page


def page1(request):
    # 查找所有用户
    user = models.User.um.all()
    #
    pagena = Paginator(user, 5)
    # 第一种方法加形参，第二种方法用GET
    pagenum = request.GET.get('pagenum')
    # 获取到指定页面的数据
    page = pagena.page(pagenum)
    return render(request, "myblog/page1.html", {"page": page})

# ====================0307================================


"发邮件"
from django.core.mail import send_mail
from django.conf import settings


def sendemail(request):
    # 主题，内容，发件人，收件人
    send_mail("hello world", "世界你好", settings.EMAIL_FROM, ['Lzj1602176692@163.com'])
    return HttpResponse("发送成功")
