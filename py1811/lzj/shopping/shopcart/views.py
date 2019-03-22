from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from . import models
from goods.models import GoodsType

@require_GET
@login_required()
def add(request, count, good_id):
    # print(count, good_id)
    # return HttpResponse("成功")
    goods = models.Goods.objects.get(pk=good_id)
    user = request.user
    try:
        shopcart = models.ShopCart.objects.get(user=user, goods=goods)
        # count是字符串
        print(type(int(count)))
        shopcart.count += int(count)
        shopcart.allTotal = shopcart.count * goods.price
        shopcart.save()
    except:
        shopcart = models.ShopCart(goods=goods, count=count, user=user)
        shopcart.count = int(count)
        shopcart.allTotal = shopcart.count * goods.price
        shopcart.save()
    return redirect(reverse("shopcart:list"))


@login_required()
def list(request):
    allGoodType = GoodsType.objects.filter(parent=None)
    shopcarts = models.ShopCart.objects.filter(user=request.user).order_by("-addTime")
    return render(request, "shopcart/list1.html", {"shopcarts": shopcarts,"allGoodType": allGoodType})


def delete(request, s_id):
    shopcart = models.ShopCart.objects.get(id=s_id)
    shopcart.delete()
    return redirect(reverse("shopcart:list"))
