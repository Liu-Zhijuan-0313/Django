"""
写视图函数的，
视图函数是用来接受请求，处理请求，做出应答
"""


from django.http import HttpResponse


# 用形式参数request接受
def index(request):
    # 简化版的处理请求
    print(request)
    # 做出应答
    return HttpResponse("hello world")


def findall(request):
    return HttpResponse("查看所有可疑人员")


def allgood(request):
    return HttpResponse("增加可疑人员")


def delete(request):
    return HttpResponse("删除可疑人员")

