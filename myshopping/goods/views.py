from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.http import HttpResponse

from . import models
from store.models import Store



def add(request, store_id):
    if request.method == "GET":
        type1 = models.GoodsType.objects.filter(parent__isnull=True)
        return render(request, "goods/add.html", {"store_id" : store_id, "type1": type1})
    else:
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        type2 = request.POST["type2"]
        intro = request.POST["intro"]
        cover = request.FILES["cover"]

        # 自己完成验证，建议使用前端+后端配合

        store = Store.objects.get(pk=store_id)
        goodsType = models.GoodsType.objects.get(pk=type2)
        goods = models.Goods(name=name, price=price, stock=stock, intro=intro, store=store, goodstype=goodsType)
        goods.save()

        goodImage = models.GoodsImage(path=cover, goods=goods)
        goodImage.save()
        return redirect(reverse("store:detail", kwargs={"s_id": store_id}))


@require_GET
def findTypeByPId(request):
    parent_id = request.GET["parent_id"]
    type2s = models.GoodsType.objects.filter(parent=parent_id)
    return HttpResponse(serialize("json", type2s))


@require_GET
def detail(request, g_id):
    goods = models.Goods.objects.get(pk=g_id)
    return render(request, "goods/detail.html", {"goods": goods})