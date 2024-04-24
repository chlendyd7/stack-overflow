from django.urls import path

from htmlwork import views

urlpatterns = [
    path('life_index', views.life_index, name='life_index'),
    path('life_sub01', views.life_sub01, name='life_sub01'),
    path('life_sub01_02', views.life_sub01_02, name='life_sub01_02'),
    path('life_sub01_03', views.life_sub01_03, name='life_sub01_03'),
    path('life_sub01_04', views.life_sub01_04, name='life_sub01_04'),

    path('life_sub02', views.life_sub02, name='life_sub02'),
    path('life_sub02_02', views.life_sub02_02, name='life_sub02_02'),
    path('life_sub02_03', views.life_sub02_03, name='life_sub02_03'),

    path('life_sub03', views.life_sub03, name='life_sub03'),

    path('life_sub04', views.life_sub04, name='life_sub04'),
    path('life_sub04_02', views.life_sub04_02, name='life_sub04_02'),

    path('life_sub04', views.life_sub04, name='life_sub04'),
    path('life_sub04_02', views.life_sub04_02, name='life_sub04_02'),
    
    path('golf_index', views.golf_index, name='golf_index'),

    path('beauty_index', views.beauty_index, name='beauty_index'),
    
    path('welfare_index', views.welfare_index, name='welfare_index'),
]
