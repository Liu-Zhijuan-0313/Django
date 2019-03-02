from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Users)
