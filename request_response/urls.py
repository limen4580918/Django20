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
    url(r'^(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather1),
    url(r'^query_str/$', views.query_str),
]