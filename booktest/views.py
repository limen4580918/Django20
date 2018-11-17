from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.


class BooksAPIView(View):
    """图书类视图"""

    def get(self):
        """GET  /books/   提供所有记录"""





        return JsonResponse()

    def post(self):
        """POST /books/   新增一条记录"""
        pass
