from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_POST
from shopcart.models import ShopCart
from goods.models import Goods
from address.models import Address
from . import models
# Create your views here.


@require_POST
def confirm(request):
    # 从购物车的list页面传过来的g_id,
    # getlist可以接受多个

    g_ids = request.POST.getlist("g_id")
    # print(g_ids)
    shopcarts = ShopCart.objects.filter(pk__in=g_ids)
    # print(shopcarts)
    addresses = Address.objects.filter(user=request.user)
    return render(request, "orders/confirm.html", {"addresses": addresses, "shopcarts": shopcarts})


def pay(request):
    # 查看第三方的一些支付接口
    # 支付宝，微信红包，银行的接口
    pass


@require_POST
def done(request):

    s_ids = request.POST.getlist("s_id")
    shopcarts = ShopCart.objects.filter(pk__in=s_ids)
    address_id = request.POST.get("address")
    address = Address.objects.get(pk=address_id)
    # address = address[0]
    # print(address)
    _address = address.recv_name + "|" + address.recv_tel + "|" + address.province + "|" + \
              address.city + "|" + address.area + "|" + address.street + "|" + address.desc
    # 生成订单
    order = models.Order(recv_address=_address, user=request.user, recv_name=address.recv_name,
                 recv_tel=address.recv_tel, all_price=0, remark="")
    order.save()
    allCotal=0
    for s in shopcarts:
        i = s.goods
        orderitem = models.OrderItem(good_id=i.id, goods_img=i.goodsimage_set.all().first().path,
                         goods_name=i.name, goods_price=i.price, goods_count=s.count,
                         goods_price_all=s.allTotal, order=order)
        orderitem.save()
        allCotal += s.allTotal
        order.all_price = allCotal
        order.save()
        return redirect(reverse("orders:list"))


def list(request):
    orders = models.Order.objects.filter(user=request.user)
    return render(request, "orders/list.html", {"orders": orders})


def detail(request, o_id):
    pass
