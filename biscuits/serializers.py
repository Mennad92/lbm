from biscuits.models import *
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'nom']
        extra_kwargs = {
            'url': {'view_name': 'category-detail', 'lookup_field': 'pk'}
        }

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='category-detail',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'description', 'category', 'price', 'stock', 'illustration']