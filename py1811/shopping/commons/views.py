from django.shortcuts import render
from goods.models import Goods, GoodsType
# Create your views here.


# 大量商品传入HTML首页
def index(request):
    # 第1个一级类型数据
    good_type1 = GoodsType.objects.filter(pk=10001)
    good_type1_2 = GoodsType.objects.filter(parent=good_type1)
    # print(good_type1_2)
    goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)[:3]
    # print(goods1_list)
    # 第2个一级类型数据
    good_type2 = GoodsType.objects.filter(pk=10002)
    good_type2_2 = GoodsType.objects.filter(parent=good_type2)
    goods2_list = Goods.objects.filter(goodstype__in=good_type2_2)
    # 第3个一级类型数据
    good_type3 = GoodsType.objects.filter(pk=10003)
    good_type3_2 = GoodsType.objects.filter(parent=good_type3)
    goods3_list = Goods.objects.filter(goodstype__in=good_type3_2)
    # 第4个一级类型数据
    good_type4 = GoodsType.objects.filter(pk=10004)
    good_type4_2 = GoodsType.objects.filter(parent=good_type4)
    goods4_list = Goods.objects.filter(goodstype__in=good_type4_2)
    # 第5个一级类型数据
    good_type5 = GoodsType.objects.filter(pk=10005)
    good_type5_2 = GoodsType.objects.filter(parent=good_type5)
    goods5_list = Goods.objects.filter(goodstype__in=good_type5_2)
    # 第6个一级类型数据
    good_type6 = GoodsType.objects.filter(pk=10006)
    good_type6_2 = GoodsType.objects.filter(parent=good_type6)
    goods6_list = Goods.objects.filter(goodstype__in=good_type6_2)
    # 第7个一级类型数据
    good_type7 = GoodsType.objects.filter(pk=10007)
    good_type7_2 = GoodsType.objects.filter(parent=good_type7)
    goods7_list = Goods.objects.filter(goodstype__in=good_type7_2)

    allGoodType = GoodsType.objects.filter(parent=None)
    return render(request, "index.html", {"allGoodType": allGoodType,
                                          "goods1_list": goods1_list,
                                          "goods2_list": goods2_list,
                                          "goods3_list": goods3_list,
                                          "goods4_list": goods4_list,
                                          "goods5_list": goods5_list,
                                          "goods6_list": goods6_list,
                                          "goods7_list": goods7_list,
                                          })


def code(request):
    pass
