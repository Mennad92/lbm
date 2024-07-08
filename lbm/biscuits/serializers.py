from biscuits.models import *
from rest_framework import serializers

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = ['url', 'id', 'nom']
        extra_kwargs = {
            'url': {'view_name': 'categorie-detail', 'lookup_field': 'pk'}
        }

class ProduitSerializer(serializers.HyperlinkedModelSerializer):
    categorie = serializers.HyperlinkedRelatedField(
        view_name='categorie-detail',
        queryset=Categorie.objects.all()
    )

    class Meta:
        model = Produit
        fields = ['url', 'id', 'nom', 'description', 'categorie', 'prix', 'stock', 'illustration']