from rest_framework import serializers
from .models import Category, Product


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(source='parent', many=False, write_only=True, queryset=Category.objects.all(), allow_null=True, required=False)
    parent = ParentSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'parent_id')
        read_only_fields = ('id', 'parent')


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source="category", many=False, write_only=True, queryset=Category.objects.all())
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'category_id', 'price')
        read_only_fields = ('id',)
