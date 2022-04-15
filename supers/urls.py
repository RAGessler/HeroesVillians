from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_post),
    path('<int:pk>/', views.super_detail)
]