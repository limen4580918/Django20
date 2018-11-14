from django.conf.urls import url
from request_response import views

"""
所有的路由都是放在url文件里边
"""

# 在urlpatterns中定义当前子应用的所有路由
urlpatterns = [
    # url(r"^正则&", views.视图);      # 子路由中一般建议以斜杠结尾,
    # 因为浏览器如果找不到该路径,会自动加一个斜杠;目的:避免用户加斜杠后导致地址不可用
    url(r'^([a-z]+)/(\d{4})/$', views.weather),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather1),
    url(r'^query_str/$', views.query_str),
    # 演示命名空间和反向解析  name一般取与子应用相同的名字,这里为了便于理解
    # name参数表示 在子路由中给路由起一个别名<以便于反向解析找到这个路由别名>
    url(r'^reverse_demo/$', views.reverse_demo, name='这是在子应用中给路由起的别名'),
    url(r'^redirect_demo/$', views.redirect_demo),
    url(r'^cookie_demo/$', views.cookie_demo),
    url(r'^session_demo/$', views.session_demo),
]