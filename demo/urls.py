"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# 在总路由中,把所有的子路由都包含进来
urlpatterns = [
    url(r'^admin/', admin.site.urls), # 默认包含一个和站点管理相关的路由

    # 使用include函数把user子应用的路由,添加到总路由列表中; 还可以设置子应用user的前缀
    # 因为是前缀<后面还要跟地址>,所以一般在主路由中,正则后面不能加$终止匹配符
    url(r'^user/', include('user.urls')),  # 同样后面的逗号别落下
    url(r'^', include('request_response.urls'))  # 这是在添加第二个子应用的路由
]
