from django.shortcuts import render
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
        pass


@require_GET
def findTypeByPId(request):
    parent_id1 = request.GET['parent_id']
    # print(parent_id)
    a = models.GoodsType.objects.get(id=parent_id1)
    type2s = models.GoodsType.objects.filter(parent=a)
    return HttpResponse(serialize("json", type2s))
