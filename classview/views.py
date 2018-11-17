from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator

#下面的两行导包 都是导入的同一个View包  可以点进去打上断点进行标记,再到第二行导入的View看是否有断点标记
from django.views import View
# from django.views.generic.base import View


# Create your views here.

def my_decorator(view_func,):
    # 直接装饰类视图里面的方法时,为了避免在中间环节出现变量值的交换,第一个形参需要手动传递self
    def wrapper(self, request, *args, **kwargs):

        print("血清生效了")
        return view_func(request, *args, **kwargs)

    return wrapper

# @my_decorator
# def get_demo(request):
#     return HttpResponse('ok')



# 使用django自带的装饰器,直接装饰这个类视图
# 原理:把我们自定义的装饰器作为第一个参数传入类视图的内部,用来装饰第二个参数所指定的方法(装饰器的引用传递)
@method_decorator(my_decorator, 'post')
# 定义类视图都要继承View类<可以调用as_view类方法>
class DemoView(View):
    """定义类视图"""
    # 直接使用我们自定义的装饰器装饰类视图里面的方法,中间环节会出现变量值的交换,不过最后又交换回来了
    # 所以直接装饰类视图里的方法时,为了避免在中间环节出现变量值的交换,自定义装饰器的内层函数第一个形参需要手动传递self
    # @my_decorator
    # 类视图里面的方法名字 一般就是我们请求方式的名字的小写<get,post..>
    def get(self, request):
        return HttpResponse('get请求业务逻辑')

    def post(self, request):
        return HttpResponse('post请求业务逻辑')