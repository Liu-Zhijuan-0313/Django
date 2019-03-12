from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models


# 测试
def index(request):
    return HttpResponse("开店")


def store_add(request):
    username = request.session['loginuser']
    user = models.Users.objects.get(username=username)
    if request.method == "GET":
        return render(request, "store/store_add.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        cover = request.POST.get("cover")
        intro = request.POST.get("intro")
        status = request.POST.get("status")

        store = models.Store(users=user, name=name, cover=cover, intro=intro, status=status)
        store.save()
        return HttpResponse("店铺添加成功")
