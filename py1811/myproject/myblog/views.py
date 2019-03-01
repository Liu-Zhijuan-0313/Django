from django.http import HttpResponse
from . import models


# 三种方法：当刷新页面的会保存数据到数据库
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


# 函数中的第一个参数request
# path：路径
# method：请求方法
# GET：表示URL?后面的内容，以字典存储数据
# GET['aa']或者GET('aa')：获取字典里建对应的值
def list3(request):
    print(request)
    # print(dir(request))
    print(request.path)
    print(request.method)
    print(request.GET)
    # print(request.GET['aa'], request.GET('bb'))
    return HttpResponse('第一个参数request')


# 响应对象????
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
    temp = loader.get_template('myblog/index.html')
    return HttpResponse(temp.render({'name': 'lzj'}, request))


# 第二种方法：响应模板
from django.shortcuts import render


def list6(request):
    # return render(request, 'myblog/index.html')
    # 带参数
    return render(request, 'myblog/index.html', {'name': 'lzj'})
