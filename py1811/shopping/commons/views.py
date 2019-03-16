from django.shortcuts import render
from goods.models import Goods, GoodsType
# Create your views here.


# 大量商品传入HTML首页
def index(request):
    allGoodType = GoodsType.objects.filter(parent=None)
    return render(request, "index.html", {"allGoodType": allGoodType})


def code(request):
    pass