from biscuits.models import *
from rest_framework import serializers


class ProduitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'