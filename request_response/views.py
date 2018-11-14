from django.http import HttpResponse, request
from django.shortcuts import render, reverse, redirect


# Create your views here.

def session_demo(request):
    """演示session的缓存读写"""
    # 设置session  session依赖于cookie
    request.session['name'] = 'laowang'
    # 存储session时,会自动生成一个session_id
    # 后面会把这个session_id通过响应对象写入到浏览器的cookie中

    # 读取session
    name = request.session.get('name')
    # 通过request对象带过来的cookie取到它里面的session_id
    # 通过session_id 到redis服务器中取到那条session记录
    # 再通过name这个键取到laowang
    print(name)
    return HttpResponse('session_demo')




def cookie_demo(request):
    response = HttpResponse('cookie_demo')
    # set_cookie方法的三个参数分别是是:键, 值, 过期时间
    response.set_cookie('name', 'laowang', 3600)

    # 浏览器第一次发起请求时request对象是没有包含cookie的
    # 需要通过response对象设置才能在下次请求时取到cookie
    name = request.COOKIES.get('name')
    print(name)


    return response


def redirect_demo(request):
    """演示重定向"""
    # redirect()接受一个参数to表示路由地址,可以重定向到另外一个路由
    # 如果参数不是以斜杠开头,则会在此视图对应的路由后面直接拼接路由地址 http://127.0.0.1:8000/redirect_demo/user/index
    # 如果是以斜杠开头则会重定向到子应用user下的index视图 http://127.0.0.1:8000/user/index
    # return redirect('/user/index')

    # 使用反向解析 动态重定向到某个视图,避免路由修改<别名没改>引起的路径错误
    return redirect(reverse('user:这是在子应用中给路由起的别名'))


def reverse_demo(request):
    """演示路由的命名空间和反响解析"""

    # 正像解析:通过路由找视图
    # 反向解析:通过视图找路由 ---> reverse()
    # 路由<域名后面,?前面的那段字符串:比如23行的'/query_str/'>
    # reverse方法返回一个路由, 参数是子应用的urls.py中给这个路由起的别名
    # url_reverse = reverse('这是在子应用中给路由起的别名')
    # 这是在总路由中定义了子路由的命名空间 后的写法
    url_reverse = reverse('request_response:这是在子应用中给路由起的别名')
    print(url_reverse)
    return HttpResponse(url_reverse)



# http://127.0.0.1:8000/query_str/?a=10&b=20&a=30/
def query_str(request):
    """演示提取字符串数据"""
    # request.GET 返回一个QueryDict 类型的对象,类似字典 但是里面可以定义同名的键
    a = request.GET.get('a')  # 一键一值 如果有同名的键,则会取到最后定义的<覆盖?>
    # 类字典对象也可以通过key取到value <注意这里是方括号!>  但是取不到会报错导致服务器错误505
    b = request.GET['b']  # 最好是用get()方法取值 取不到则返回None,不会报错;
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