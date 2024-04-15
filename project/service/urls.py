from rest_framework import routers
from service import views
from django.urls import path, include

router = routers.DefaultRouter(trailing_slash=False)
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
