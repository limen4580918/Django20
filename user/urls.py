from django.conf.urls import url
from user import views

"""
所有的路由都是放在url文件里边
"""

# 在urlpatterns中定义当前子应用的所有路由
urlpatterns = [
    # url(r"^正则&", views.视图);      # 子路由中一般建议以斜杠结尾,
    # 因为浏览器如果找不到该路径,会自动加一个斜杠;目的:避免用户加斜杠后导致地址不可用
    url(r'^index/$', views.index),
    url(r'^index_info$', views.index_info),

    # 演示在不同子应用中取相同路由别名<request_response中也定义了一个相同别名>
    url(r'^say$', views.say, name='这是在子应用中给路由起的别名'),
]