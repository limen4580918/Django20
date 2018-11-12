from django.shortcuts import render, reverse
from django.http import HttpResponse
# Create your views here.

# 视图函数的第一个传入参数必须定义，用于接收Django构造的包含了请求数据的HttpRequest对象，通常名为request
def index(request):
    """
    index 视图
    :param request: 包含请求信息的请求对象
    :return: 返回响应对象
    """
    return HttpResponse("hello Django!")


def index_info(request):
    return HttpResponse("index_info")


def say(request):
    """演示在不同子应用中取相同路由别名"""
    # reverse方法返回一个路由, 参数是子应用的urls.py中给这个路由起的别名
    url_say = reverse('这是在子应用中给路由起的别名')
    print(url_say)
    return HttpResponse(url_say)