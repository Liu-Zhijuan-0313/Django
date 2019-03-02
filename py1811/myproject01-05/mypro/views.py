"""
写视图函数的，
视图函数是用来接受请求，处理请求，做出应答
"""


from django.http import HttpResponse


# # 用形式参数request接受
# def index1(request):
#     # 简化版的处理请求
#     print(request)
#     # 做出应答
#     return HttpResponse("hello world")

# =====================================================


from django.shortcuts import render


# 静态资源
def index1(request):
    return render(request, "index1.html", {})


# 主页面的视图函数
def base(request):
    return render(request, "base.html")


# 继承主页面的子页面的视图函数
def base_index1(request):
    return render(request, "base_index1.html")
