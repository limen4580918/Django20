# 定义中间件函数

def my_middleware1(get_response):
    print("初始化中间件1")

    def middleware(request):

        print("before request 1被调用")

        response = get_response(request)

        print('after response 1被调用')

        return response

    return middleware