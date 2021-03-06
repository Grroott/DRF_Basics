from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.mixins import CreateModelMixin


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
