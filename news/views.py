from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print(request)
    return HttpResponse('Hello World')

def test(request):
    return HttpResponse('<h1>Тест страница</h1>')