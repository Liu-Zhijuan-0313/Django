from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from shopcart.models import ShopCart
from goods.models import Goods
from address.models import Address
from goods.models import GoodsType
from . import models
# Create your views here.


def confirm(request):
    # 从购物车的list页面传过来的g_id,
    # getlist可以接受多个
    if request.method == "GET":
        return render(request, "orders/confirm1.html")
    if request.method == "POST":
        g_ids = request.POST.getlist("g_id")
        # print(g_ids)
        shopcarts = ShopCart.objects.filter(pk__in=g_ids)
        # print(shopcarts)
        addresses = Address.objects.filter(user=request.user)
        return render(request, "orders/confirm1.html", {"addresses": addresses, "shopcarts": shopcarts})


def pay(request):
    # 查看第三方的一些支付接口
    # 支付宝，微信红包，银行的接口
    pass


@require_POST
def done(request):
    s_ids = request.POST.getlist("s_id")
    shopcarts = ShopCart.objects.filter(pk__in=s_ids)
    address_id = request.POST.get("goods")
    address = Address.objects.get(pk=address_id)
    # goods = goods[0]
    # print(goods)
    _address = address.recv_name + "|" + address.recv_tel + "|" + address.province + "|" + \
              address.city + "|" + address.area + "|" + address.street + "|" + address.desc
    # 生成订单
    order = models.Order(recv_address=_address, user=request.user, recv_name=address.recv_name,
                 recv_tel=address.recv_tel, all_price=0, remark="")
    order.save()
    allCotal=0
    for s in shopcarts:
        i = s.goods
        # print(i)
        orderitem = models.OrderItem(good_id=i.id, goods_img=i.goodsimage_set.all().first().path,
                         goods_name=i.name, goods_price=i.price, goods_count=s.count,
                         goods_price_all=s.allTotal, order=order)
        orderitem.save()
        allCotal += s.allTotal
        order.all_price = allCotal
        order.save()
        return redirect(reverse("orders:list"))


@login_required()
def list(request):
    allGoodType = GoodsType.objects.filter(parent=None)
    orders = models.Order.objects.filter(user=request.user)
    return render(request, "orders/list1.html", {"orders": orders,"allGoodType": allGoodType})


def detail(request, o_id):
    order = models.Order.objects.get(id=o_id)
    return render(request, "orders/detail1.html", {"order": order})


def delete(request, o_id):
    orders = models.Order.objects.get(id=o_id)
    orders.delete()
    return redirect(reverse("orders:list"))

