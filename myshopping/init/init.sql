# 一级类型
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10001, '点心/蛋糕', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10002, '鞋靴 / 箱包 / 配件', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10003, '童装玩具 / 孕产 / 用品', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10004, '家电 / 数码 / 手机', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10005, '美妆 / 洗护 / 保健品', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10006, '珠宝 / 眼镜 / 手表', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10007, '运动 / 户外 / 乐器', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10008, '游戏 / 动漫 / 影视', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10009, '美食 / 生鲜 / 零食', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10010, '鲜花 / 宠物 / 农资', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10011, '房产 / 装修 / 建材', 'static/images/goods/default.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10012, '家具 / 家饰 / 家纺装', 'static/images/goods/default.png', '', null);


# 二级类型
-- 女装 / 男装 / 内衣
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200001, '蛋糕', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200002, '蒸蛋糕', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200003, '脱水蛋糕', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200004, '瑞士卷', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200005, '软面包', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200006, '马卡龙', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200007, '千层饼', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200008, '甜甜圈', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200009, '蒸三明治', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200010, '铜锣烧', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200011, '点心', 'static/images/goods/default.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200012, '蒸蛋糕', 'static/images/goods/default.png', '', 10001);


-- 鞋靴 / 箱包 / 配件
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100001, '女鞋', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100002, '红人同款', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100003, '夏上新', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100004, '一脚蹬', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100005, '平底鞋', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100006, '复古方头', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100007, '爸爸鞋', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100008, '正装商务', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100009, '增高鞋', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100010, '豆豆鞋', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100011, '男鞋', 'static/images/goods/default.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100012, '帆布鞋', 'static/images/goods/default.png', '', 10002);



-- 童装玩具 / 孕产 / 用品
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300001, '内衣3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300002, '正装3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300003, '西裤3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300004, '衬衫3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300005, '衬衫33', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300006, '裙子3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300007, '帽子3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300008, '连衣3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300009, '牛仔3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300010, '蕾丝3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300011, '丝光3', 'static/images/goods/default.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300012, '睡裙3', 'static/images/goods/default.png', '', 10003);


-- 家电 / 数码 / 手机
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400001, '内衣4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400002, '正装4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400003, '西裤4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400004, '衬衫4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400005, '衬衫44', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400006, '裙子4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400007, '帽子4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400008, '连衣4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400009, '牛仔4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400010, '蕾丝4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400011, '丝光4', 'static/images/goods/default.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400012, '睡裙4', 'static/images/goods/default.png', '', 10004);


-- 美妆 / 洗护 / 保健品
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500001, '内衣5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500002, '正装5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500003, '西裤5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500004, '衬衫5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500005, '衬衫55', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500006, '裙子5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500007, '帽子5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500008, '连衣5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500009, '牛仔5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500010, '蕾丝5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500011, '丝光5', 'static/images/goods/default.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500012, '睡裙5', 'static/images/goods/default.png', '', 10005);


-- 珠宝 / 眼镜 / 手表
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600001, '内衣6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600002, '正装6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600003, '西裤6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600004, '衬衫6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600005, '衬衫66', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600006, '裙子6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600007, '帽子6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600008, '连衣6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600009, '牛仔6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600010, '蕾丝6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600011, '丝光6', 'static/images/goods/default.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600012, '睡裙6', 'static/images/goods/default.png', '', 10006);



-- 运动 / 户外 / 乐器
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700001, '内衣7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700002, '正装7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700003, '西裤7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700004, '衬衫7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700005, '衬衫77', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700006, '裙子7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700007, '帽子7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700008, '连衣7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700009, '牛仔7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700010, '蕾丝7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700011, '丝光7', 'static/images/goods/default.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700012, '睡裙7', 'static/images/goods/default.png', '', 10007);



-- 游戏 / 动漫 / 影视
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800001, '内衣8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800002, '正装8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800003, '西裤8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800004, '衬衫88', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800005, '衬衫8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800006, '裙子8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800007, '帽子8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800008, '连衣8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800009, '牛仔8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800010, '蕾丝8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800011, '丝光8', 'static/images/goods/default.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800012, '睡裙8', 'static/images/goods/default.png', '', 10008);



-- 美食 / 生鲜 / 零食
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900001, '内衣9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900002, '正装9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900003, '西裤9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900004, '衬衫9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900005, '衬衫99', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900006, '裙子9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900007, '帽子9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900008, '连衣9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900009, '牛仔9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900010, '蕾丝9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900011, '丝光9', 'static/images/goods/default.png', '', 10009);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(900012, '睡裙9', 'static/images/goods/default.png', '', 10009);


-- 鲜花 / 宠物 / 农资
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000001, '内衣10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000002, '正装10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000003, '西裤10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000004, '衬衫102', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000005, '衬衫10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000006, '裙子10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000007, '帽子10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000008, '连衣10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000009, '牛仔10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000010, '蕾丝10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000011, '丝光10', 'static/images/goods/default.png', '', 10010);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1000012, '睡裙10', 'static/images/goods/default.png', '', 10010);

-- 房产 / 装修 / 11材
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100001, '内衣11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100002, '正装11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100003, '西裤11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100004, '衬衫1111', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100005, '衬衫11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100006, '裙子11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100007, '帽子11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100008, '连衣11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100009, '牛仔11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100010, '蕾丝11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100011, '丝光11', 'static/images/goods/default.png', '', 10011);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1100012, '睡裙11', 'static/images/goods/default.png', '', 10011);


-- 家具 / 家饰 / 家纺装
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200001, '内衣', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200002, '正装', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200003, '西裤', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200004, '衬衫', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200005, '衬衫', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200006, '裙子', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200007, '帽子', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200008, '连衣', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200009, '牛仔', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200010, '蕾丝', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200011, '丝光', 'static/images/goods/default.png', '', 10012);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(1200012, '睡裙', 'static/images/goods/default.png', '', 10012);

