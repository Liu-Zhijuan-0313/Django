from django.db import models

# Create your models here.
"""
6.ORM：对象关系映射
程序中是一对象存在，数据库其中是以关系表存在
映射：
       1.一个类对应一个表
       2.类的一个属性对应表的一列
       3. 类对应的一个对象的属性值
"""


# 定义类的管理器
class UsersManger(models.Manager):
    def createUser(self, name, age):
        au = self.create(name=name, age=age)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=16)

    # @classmethod
    # def create(cls, name, age):
    #     au = cls(name=name, age=age)
    #     return au

    # 通过属性的方式指向类的管理器
    um = UsersManger()


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User)


"""
连接数据库：
1.建立库
2.下载数据库的连接驱动：pymysql
3. 引入数据库驱动（在根模块的__init__.py中引入，并做伪装，pymysql伪装为MySQLdb）
   import pymysql
   pymysql.install_as_MySQLdb()
4.连接的设置setting
   DATABASES = {
        'default': {
            'ENGINE‘: 'django.db.backends.mysql', #数据库引擎
            'NAME': 'goods', #数据库名
            'USER': 'root',  #用户名  
            'PASSWORD': '123456', #密码
         }
   } 
5.定义模型models.py
6.生成迁移文件：
    python  manage.py  makemigrations
查看生成的sql语句：
    python manage.py sqlmigrate 子模块名如：myblog 生成的文件如：0001
7.执行数据库同步：python  manage.py  migrate
"""
