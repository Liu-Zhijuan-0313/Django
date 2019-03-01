from django.db import models

# Create your models here.


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
