from django.urls import path
from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
]