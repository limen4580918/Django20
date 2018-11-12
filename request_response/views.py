from django.http import HttpResponse
from django.shortcuts import render, reverse

# Create your views here.

def reverse_demo(request):
    """演示路由的命名空间和反响解析"""

    # 正像解析:通过路由找视图
    # 反向解析:通过视图找路由
    # 路由<域名后面,?前面的那段字符串:比如23行的'/query_str/'>
    # reverse方法返回一个路由, 参数是子应用的urls.py中给这个路由起的别名
    url_reverse = reverse('这是在子应用中给路由起的别名')
    print(url_reverse)
    return HttpResponse(url_reverse)








# http://127.0.0.1:8000/query_str/?a=10&b=20&a=30/
def query_str(request):
    """演示提取字符串数据"""
    # request.GET 返回一个QueryDict 类型的对象,类似字典 但是里面可以定义同名的键
    # a = request.GET['key']  # 类字典对象也可以通过key取到value <注意这里是方括号!>
    a = request.GET.get('a')  # 一键一值 如果有同名的键,则会取到最后定义的<覆盖?>
    b = request.GET['b']
    c = request.GET.getlist('a')  # 一键多值,返回一个列表
    print(a, b, c)
    return HttpResponse('query_str')

def weather(request, city, year):
    print('city=%s'% city)
    print('year=%s'% year)
    return HttpResponse('ok')

def weather1(request, city, year):
    print('city1=%s'% city)
    print('year1=%s'% year)
    return HttpResponse('ok')