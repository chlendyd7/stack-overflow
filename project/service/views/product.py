from django.shortcuts import render
from rest_framework import viewsets
from service.models.product import Product
from rest_framework.response import Response
# from services.product import ProductService


class ProductViewSet(viewsets.ViewSet):
    queryset=Product.objects.all()
    

    # def create(self, request):
    #     product_repo = ProductService()

    def list(self, request):
        p=Product.objects.all()
        for p1 in p:
            print(p1)
        queryset=self.queryset
        print(queryset)
        return Response('공사중')
