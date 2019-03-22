from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.http import HttpResponse
from . import models
from goods.models import Goods, GoodsType
# Create your views here.
# 商品添加


# def add(request):
#     if request.method == "GET":
#         return render(request, "goods/add.html")
#     elif request.method == "POST":
#         name = request.POST["name"]
#         price = request.POST["price"]
#         stock = request.POST["stock"]
#         intro = request.POST["intro"]
#         cover = request.FILES["cover"]
#
#         store_id = request.POST["store_id"]
#         store = models.Store.objects.get(id=store_id)
#         type2 = request.POST["type2"]
#         goodstype = models.GoodsType.objects.get(id=type2)
#
#         goods = models.Goods(name=name, price=price, stock=stock, intro=intro, stores=store, goodstype=goodstype)
#         goods.save()
#         goodsimage = models.GoodsImage(path=cover, goods=goods)
#         goodsimage.save()
#         return redirect(reverse("store:detail", kwargs={"s_id": store_id}))


def add(request, s_id):
    if request.method == "GET":
        store = models.Store.objects.get(pk=s_id)
        type1 = GoodsType.objects.filter(parent=None)
        goods = Goods.objects.filter(stores=store)
        return render(request, "goods/add1.html", {"s_id": s_id, "store": store, "type1": type1, "goods": goods})
    elif request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        intro = request.POST["intro"]
        cover = request.FILES["cover"]

        # store_id = request.POST["store_id"]
        store = models.Store.objects.get(id=s_id)
        type2 = request.POST["type2"]
        goodstype = models.GoodsType.objects.get(id=type2)

        goods = models.Goods(name=name, price=price, stock=stock, intro=intro, stores=store, goodstype=goodstype)
        goods.save()
        goodsimage = models.GoodsImage(path=cover, goods=goods)
        goodsimage.save()
        return redirect(reverse("store:detail", kwargs={"s_id": s_id}))



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
    return render(request, "goods/detail1.html", {"goods": goods})


def list(request):
    goods = models.Goods.objects.all()
    return render(request, "goods/list.html", {"goods": goods})
    # # 第1个一级类型数据
    # good_type1 = GoodsType.objects.filter(pk=10001)
    # good_type1_2 = GoodsType.objects.filter(parent=good_type1)
    # # print(good_type1_2)
    # goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)[:3]
    # # print(goods1_list)
    # # 第2个一级类型数据
    # good_type2 = GoodsType.objects.filter(pk=10002)
    # good_type2_2 = GoodsType.objects.filter(parent=good_type2)
    # goods2_list = Goods.objects.filter(goodstype__in=good_type2_2)
    # # 第3个一级类型数据
    # good_type3 = GoodsType.objects.filter(pk=10003)
    # good_type3_2 = GoodsType.objects.filter(parent=good_type3)
    # goods3_list = Goods.objects.filter(goodstype__in=good_type3_2)
    # # 第4个一级类型数据
    # good_type4 = GoodsType.objects.filter(pk=10004)
    # good_type4_2 = GoodsType.objects.filter(parent=good_type4)
    # goods4_list = Goods.objects.filter(goodstype__in=good_type4_2)
    # # 第5个一级类型数据
    # good_type5 = GoodsType.objects.filter(pk=10005)
    # good_type5_2 = GoodsType.objects.filter(parent=good_type5)
    # goods5_list = Goods.objects.filter(goodstype__in=good_type5_2)
    # # 第6个一级类型数据
    # good_type6 = GoodsType.objects.filter(pk=10006)
    # good_type6_2 = GoodsType.objects.filter(parent=good_type6)
    # goods6_list = Goods.objects.filter(goodstype__in=good_type6_2)
    # # 第7个一级类型数据
    # good_type7 = GoodsType.objects.filter(pk=10007)
    # good_type7_2 = GoodsType.objects.filter(parent=good_type7)
    # goods7_list = Goods.objects.filter(goodstype__in=good_type7_2)
    #
    # return render(request, "list.html", {
    #                                        "goods1_list": goods1_list,
    #                                        "goods2_list": goods2_list,
    #                                        "goods3_list": goods3_list,
    #                                        "goods4_list": goods4_list,
    #                                        "goods5_list": goods5_list,
    #                                        "goods6_list": goods6_list,
    #                                        "goods7_list": goods7_list,
    #                                        })

