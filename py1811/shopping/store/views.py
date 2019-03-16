from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
# Create your views here.
from . import models
from goods.models import GoodsType


# 添加店铺
@login_required()
def add(request):
    if request.method == "GET":
        return render(request, "store/add.html", {})
    else:
        name = request.POST['name']
        intro = request.POST['intro']
        try:
            cover = request.FILES['cover']
            store = models.Store(name=name, intro=intro, cover=cover, user=request.user)
        except:
            store = models.Store(name=name, intro=intro, user=request.user)
        store.save()
        # return redirect(reverse("store:detail", kwargs={"s_id": store.id}))
        return redirect(reverse("store:list"))


@require_GET
@login_required()
def list(request):
    store = models.Store.objects.filter(user=request.user, status__in=[0, 1])
    return render(request, "store/list.html", {"store": store})


@login_required()
def update(request, s_id):
    if request.method == "GET":
        store = models.Store.objects.get(pk=s_id)
        return render(request, "store/update.html", {"store": store})
    else:
        name = request.POST['name']
        intro = request.POST['intro']
        "找到store对象，直接按照（对象.属性 = 属性值）赋值"
        store = models.Store.objects.get(pk=s_id)
        store.name = name
        store.intro = intro
        try:
            cover = request.FILES['cover']
            # store = models.Store(name=name, intro=intro, cover=cover, user=request.user)
            store.cover = cover
        except:
            pass
            # store = models.Store(name=name, intro=intro, user=request.user)
        store.save()
        # return redirect(reverse("store:detail", kwargs={"s_id": store.id}))
        return redirect(reverse("store:detail", kwargs={"s_id": store.id}))


@require_GET
@login_required()
def detail(request, s_id):
    store = models.Store.objects.get(pk=s_id)
    type1 = GoodsType.objects.filter(parent=None)
    return render(request, "store/detail.html", {"store": store, "type1": type1})


# 店铺状态
@require_GET
@login_required()
def change(request, s_id, status):
    store = models.Store.objects.get(id=s_id)
    store.status = int(status)
    store.save()
    if store.status == 2:
        return redirect(reverse("store:list"))
    else:
        return render(request, "store/detail.html", {"store": store})
