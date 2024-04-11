from django.shortcuts import render
from rest_framework import viewsets
from project.service.services.product import ProductService


class ProductViewSet(viewsets.ViewSet):

    def create(self, request):
        product_repo = ProductService()
