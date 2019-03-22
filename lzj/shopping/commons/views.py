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
    # 第8个一级类型数据
    good_type8 = GoodsType.objects.filter(pk=10008)
    good_type8_2 = GoodsType.objects.filter(parent=good_type8)
    goods8_list = Goods.objects.filter(goodstype__in=good_type8_2)

    # 第9个一级类型数据
    good_type9 = GoodsType.objects.filter(pk=10009)
    good_type9_2 = GoodsType.objects.filter(parent=good_type9)
    goods9_list = Goods.objects.filter(goodstype__in=good_type9_2)

    # 第10个一级类型数据
    good_type10 = GoodsType.objects.filter(pk=100010)
    good_type10_2 = GoodsType.objects.filter(parent=good_type10)
    goods10_list = Goods.objects.filter(goodstype__in=good_type10_2)

    # 第11个一级类型数据
    good_type11 = GoodsType.objects.filter(pk=100011)
    good_type11_2 = GoodsType.objects.filter(parent=good_type11)
    goods11_list = Goods.objects.filter(goodstype__in=good_type11_2)
    # 第12个一级类型数据
    good_type12 = GoodsType.objects.filter(pk=100012)
    good_type12_2 = GoodsType.objects.filter(parent=good_type12)
    goods12_list = Goods.objects.filter(goodstype__in=good_type12_2)

    # 第13个一级类型数据
    good_type13 = GoodsType.objects.filter(pk=100013)
    good_type13_2 = GoodsType.objects.filter(parent=good_type13)
    goods13_list = Goods.objects.filter(goodstype__in=good_type13_2)

    # 第14个一级类型数据
    good_type14 = GoodsType.objects.filter(pk=100014)
    good_type14_2 = GoodsType.objects.filter(parent=good_type14)
    goods14_list = Goods.objects.filter(goodstype__in=good_type14_2)
    allGoodType = GoodsType.objects.filter(parent=None)
    return render(request, "index1.html", {"allGoodType": allGoodType,
                                          "goods1_list": goods1_list,
                                          "goods2_list": goods2_list,
                                          "goods3_list": goods3_list,
                                          "goods4_list": goods4_list,
                                          "goods5_list": goods5_list,
                                          "goods6_list": goods6_list,
                                          "goods7_list": goods7_list,
                                          "goods8_list": goods8_list,
                                          "goods9_list": goods9_list,
                                          "goods10_list": goods10_list,
                                          "goods11_list": goods11_list,
                                          "goods12_list": goods12_list,
                                          "goods13_list": goods13_list,
                                          "goods14_list": goods14_list,
                                          })


def base(request):
    allGoodType = GoodsType.objects.filter(parent=None)
    return render(request, "base.html", {"allGoodType": allGoodType})
