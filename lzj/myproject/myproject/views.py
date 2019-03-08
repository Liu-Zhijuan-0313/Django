from django.http import HttpResponse
from django.shortcuts import render


# 项目首页面
def base(request):
    print("哈哈哈哈", request.session.get("loginUser"))
    return render(request, "base.html", {"request": request})
