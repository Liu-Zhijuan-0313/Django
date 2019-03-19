from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.http import HttpResponse
from . import models
# Create your views here.
# 商品添加


def add(request):
    if request.method == "GET":
        return render(request, "")
    else:
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        intro = request.POST["intro"]
        cover = request.FILES["cover"]

        store_id = request.POST["store_id"]
        store = models.Store.objects.get(id=store_id)
        type2 = request.POST["type2"]
        goodstype = models.GoodsType.objects.get(id=type2)

        goods = models.Goods(name=name, price=price, stock=stock, intro=intro, stores=store, goodstype=goodstype)
        goods.save()
        goodsimage = models.GoodsImage(path=cover, goods=goods)
        goodsimage.save()
        return redirect(reverse("store:detail", kwargs={"s_id": store_id}))


@require_GET
def findTypeByPId(request):
    parent_id1 = request.GET['parent_id']
    # print(parent_id)
    a = models.GoodsType.objects.get(id=parent_id1)
    type2s = models.GoodsType.objects.filter(parent=a)
    return HttpResponse(serialize("json", type2s))


@require_GET
def detail(request, g_id):
    goods = models.Goods.objects.get(id=g_id)
    return render(request, "goods/detail.html", {"goods": goods})
