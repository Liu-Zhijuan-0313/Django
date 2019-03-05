# 表单封装
from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=2, label="姓名")
    age = forms.IntegerField(label="年龄")

