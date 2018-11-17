from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^books/$',views.BooksAPIView.as_view()),
]