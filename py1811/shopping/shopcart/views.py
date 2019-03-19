from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from . import models

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


def list(request):
    shopcarts = models.ShopCart.objects.filter(user=request.user).order_by("-addTime")
    return render(request, "shopcart/list.html", {"shopcarts": shopcarts})

