from django.shortcuts import render
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
