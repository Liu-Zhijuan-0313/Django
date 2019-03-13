from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from . import models


# 测试
def index(request):
    return HttpResponse("开店")


# 1.添加店铺
def store_add(request):
    # 判断是否登录
    try:
        username1 = request.session['loginuser']
        user = models.Users.objects.get(username=username1)
    except:
        return redirect(reverse("users:login"))

    user = models.Users.objects.get(username=username1)
    if request.method == "GET":
        return render(request, "store/store_add.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        cover = request.FILES["cover"]
        intro = request.POST.get("intro")
        status = request.POST.get("status")

        store = models.Store(users=user, name=name, cover=cover, intro=intro, status=status)
        store.save()
        return HttpResponse("店铺添加成功")


# 2.店铺列表
def store_list(request):
    if request.method == "GET":
        # 判断是否登录
        try:
            username1 = request.session['loginuser']
            user = models.Users.objects.get(username=username1)
        except:
            return redirect(reverse("users:login"))
        storeall = models.Store.objects.filter(users=user)
        return render(request, "store/store_list.html", {"storeall": storeall})


# 3.店铺详情
def store_detail(request, id):
    if request.method == "GET":
        store = models.Store.objects.get(id=id)
        return render(request, "store/store_detail.html", {"store": store})


# 4.修改店铺信息
def store_update(request, id):
    # 判断是否登录
    try:
        username1 = request.session['loginuser']
        user = models.Users.objects.get(username=username1)
    except:
        return redirect(reverse("users:login"))

    store1 = models.Store.objects.get(id=id)
    if request.method == "GET":
        return render(request, "store/store_update.html", {"store": store1})
    elif request.method == "POST":
        name = request.POST.get("name")
        intro = request.POST.get("intro")
        status = request.POST.get("status")

        store = models.Store(id=id, users=user, name=name, cover=store1.cover, intro=intro, status=status,opener_time=store1.opener_time)
        store.save()
        return redirect(reverse("store:store_detail", args=(store.id,)))


# 5.店铺状态 # 0 正常营业 1 暂停营业 2 永久删除
def store_delete(request, id):
    if request.method == "GET":
        store = models.Store.objects.get(id=id)
        store.delete()
        return redirect(reverse("store:store_list"))


# 6.修改店铺封面
def store_update_img(request, id):
    # 判断是否登录
    try:
        username1 = request.session['loginuser']
        user = models.Users.objects.get(username=username1)
    except:
        return redirect(reverse("users:login"))
    store1 = models.Store.objects.get(id=id)
    if request.method == "GET":
        return render(request, "store/store_update_img.html", {"store": store1})
    elif request.method == "POST":
        cover = request.FILES["cover"]
        store = models.Store(id=id, users=user, name=store1.name,intro=store1.intro, status=store1.status, cover=cover, opener_time=store1.opener_time)
        store.save()
        return redirect(reverse("store:store_detail", args=(store.id,)))
