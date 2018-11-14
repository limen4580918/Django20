from django.conf.urls import url

from classview import views

urlpatterns = [
    # 路由后面加斜杠,用postman使用POST请求不加会报错,而GET不会报错
    # url(r'^classview/', views.DemoView.as_view()),

    # 在路由中使用自定义装饰器,装饰as_view返回的那个结果(视图函数)
    # 缺点是这个装饰器会装饰类视图中的所有方法; 解决方法:在视图views.py中给某个具体方法加装饰器
    url(r'^classview/', views.my_decorator(views.DemoView.as_view())),

]