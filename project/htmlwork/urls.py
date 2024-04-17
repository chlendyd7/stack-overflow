from django.urls import path

from .views import ttest

urlpatterns = [
    path('test', ttest)
]
