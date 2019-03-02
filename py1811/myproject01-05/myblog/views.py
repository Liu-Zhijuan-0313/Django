from django.http import HttpResponse
from . import models


"三种方法：当刷新页面的会保存数据到数据库"


def index(req):

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
def register(request):
    if request.method == "GET":
        return render(request, "myblog/register.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        print(name, age)
        user = models.User(name=name, age=age)
        user.save()
        return HttpResponse("注册成功")


# 后台数据库有这个用户则登录成功，没有则重新登录
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
