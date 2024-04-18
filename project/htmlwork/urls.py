from django.urls import path

from htmlwork import views

urlpatterns = [
    path('test', views.life_index),
    path('sub02', views.life_sub02),
    path('sub02_02', views.life_sub02_02),
]
