from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from . import models
from users.models import Userinfo

# 1.添加地址
def address_add(request):
    if request.method == "GET":
        return render(request, "address/add_address1.html")
    elif request.method == "POST":
        recv_name = request.POST["recv_name"]
        recv_tel = request.POST["recv_tel"]
        province = request.POST["province"]
        city = request.POST["city"]
        area = request.POST["area"]
        street = request.POST["street"]
        desc = request.POST["desc"]


        try:
            # 说明这个地址设为默认
            # Q查询对象
            request.POST["is_default"]
            # 查自己的所有地址，把地址都设置为不默认
            address = models.Address.objects.filter(user=request.user)
            for i in address:
                i.is_default = False
                i.save()
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel,
                                         province=province, city=city, area=area, street=street,
                                         desc=desc, user=request.user, is_default=True)
            address.save()

        except:
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel,
                           province=province, city=city, area=area, street=street,
                           desc=desc, user=request.user)
            address.save()

        return redirect(reverse("address:address_list"))


# 2.地址列表
def address_list(request):
    address = models.Address.objects.filter(user=request.user)
    # print(address)
    return render(request, "address/address_list1.html", {"address": address})


# 3.查看地址详情
def address_read(request, id):
    if request.method == "GET":
        address = models.Address.objects.get(id=id)
        return render(request, "address/address_read1.html", {"address": address})


# 4.删除地址
def address_delete(request, id):
    address = models.Address.objects.get(id=id)
    address.delete()
    return redirect(reverse("address:address_list"))


# 5.修改地址
def address_update(request, id):
    address1 = models.Address.objects.get(id=id)
    if request.method == "GET":
        return render(request, "address/address_update1.html", {"address": address1})
    elif request.method == "POST":
        recv_name = request.POST.get("recv_name")
        recv_tel = request.POST.get("recv_tel")
        province = request.POST.get("province")
        city = request.POST.get("city")
        area = request.POST.get("area")
        street = request.POST.get("street")
        desc = request.POST.get("desc")

        try:
            request.POST.get("is_default")
            address = models.Address.objects.filter(user=request.user)
            for i in address:
                i.is_default = False
                i.save()
            address = models.Address(id=id, recv_name=recv_name, recv_tel=recv_tel, province=province,
                                     city=city, area=area, street=street, desc=desc,
                                     is_default=True, user=request.user)
            address.save()
        except:
            address = models.Address(id=id, recv_name=recv_name, recv_tel=recv_tel, province=province,
                                     city=city, area=area, street=street, desc=desc,
                                      user=request.user)
            address.save()
        return redirect(reverse("address:address_read", args=(address.id,)))
        # return HttpResponse("成功")
