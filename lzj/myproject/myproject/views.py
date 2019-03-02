from django.http import HttpResponse


def index(request):
    return HttpResponse("博客首页面")