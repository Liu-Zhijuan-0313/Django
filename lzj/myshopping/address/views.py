from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from . import models
from users.models import Users


# 测试
def index(request):
    return render(request, "address/address_add.html")


# 添加地址
def address_add(request):
    if request.method == "GET":
        return render(request, "address/address_add.html")
    elif request.method == "POST":
        recv_name = request.POST.get("recv_name")
        recv_phone = request.POST.get("recv_phone")
        native = request.POST.get("native")
        provice = request.POST.get("provice")
        city = request.POST.get("city")
        country = request.POST.get("country")
        street = request.POST.get("street")
        desc = request.POST.get("desc")
        status = request.POST.get("status")

        # 获取登录用户，外键必须为是一个对象, 无法分配“'lzj'”:“地址。用户必须是一个“用户”实例
        username = request.session['loginuser']
        user = models.Users.objects.get(username=username)

        address = models.Address(users=user, recv_name=recv_name, recv_phone=recv_phone, native=native,
                       provice=provice, city=city, country=country, street=street, desc=desc, status=status)
        address.save()
        # return HttpResponse("地址添加完成")
        return redirect(reverse("address:address_readlist"))


# 查看所有地址
def address_readlist(request):
    if request.method == "GET":
        # 查看此用户的所有地址，不能参看其他人的地址
        username = request.session['loginuser']
        user = models.Users.objects.get(username=username)
        addressall = models.Address.objects.filter(users_id=user.id)
        print(addressall)
        for i in addressall:
            print(i.recv_name)
        return render(request, "address/address_readlist.html", {"addressall": addressall})


# 查看地址详情
def address_read(request, id):
    if request.method == "GET":
        address = models.Address.objects.get(id=id)

        return render(request, "address/address_read.html",{"address": address})


# 删除地址
def address_delete(request, id):
    address = models.Address.objects.get(id=id)
    address.delete()
    return redirect(reverse("address:address_readlist"))


# 修改地址
def address_update(request, id):
    address1 = models.Address.objects.get(id=id)
    user = models.Users.objects.get(id=address1.users.id)
    if request.method == "GET":
        return render(request, "address/address_update.html", {"address": address1})
    elif request.method == "POST":
        recv_name = request.POST.get("recv_name")
        recv_phone = request.POST.get("recv_phone")
        native = request.POST.get("native")
        provice = request.POST.get("provice")
        city = request.POST.get("city")
        country = request.POST.get("country")
        street = request.POST.get("street")
        desc = request.POST.get("desc")
        status = request.POST.get("status")

        address = models.Address(id=address1.id, users=user, recv_name=recv_name, recv_phone=recv_phone, native=native, provice=provice,
                       city=city, country=country, street=street, desc=desc, status=status)
        address.save()
        return redirect(reverse("address:address_read", args=(address.id,)))

