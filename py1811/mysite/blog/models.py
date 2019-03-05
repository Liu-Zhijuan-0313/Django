from django.db import models

# Create your models here.


# class UserManger(models.Manager):
#     def createuser(self, name, age):
#         au = self.create(name=name, age=age)
#
#
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     age = models.IntegerField(max_length=20)
#
#
#     @classmethod
#     def create(cls, name, age):
#         au = cls(name=name, age=age)
#         return au
#     um = UserManger()


class Userregister(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Userregister)




