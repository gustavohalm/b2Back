from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ('name', 'parent')
    pagination_class = None

    @action(url_path="parents", detail=False)
    def parents(self, request):
        categories = Category.objects.filter(parent=None)
        return Response(CategorySerializer(categories, many=True).data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    filterset_fields = ('name', 'category')
