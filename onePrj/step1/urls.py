# 새로 생성후 소스 삽입
from django.urls import path
from . import views

# 시작페이지 주소와 뷰함수 연결
urlpatterns = [
    # /step1/ 주소
    path('', views.index),
    # /step1/sub1/
    path('sub1/', views.sub1),
]
