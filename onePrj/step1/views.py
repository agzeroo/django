from django.shortcuts import render
from django.http import HttpResponse

# /, /step1/ 주소와 연결되는 뷰함수


def index(request):
    return HttpResponse("<h1>Hello world</h1>")

# /step1/sub1 주소와 연결되는 뷰함수


def sub1(request):
    return render(request, 'step1/sub1.html')
# Create your views here.
