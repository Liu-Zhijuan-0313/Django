from django.shortcuts import render, redirect, reverse

# Create your views here.
from . import models


def address_add(request):
    if request.method == "GET":
        return render(request, "address/add_address.html")
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


def address_list(request):
    address = models.Address.objects.filter(user=request.user)
    # print(address)
    return render(request, "address/address_list.html", {"address": address})
