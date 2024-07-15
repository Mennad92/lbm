from biscuits.models import *
from rest_framework import permissions, viewsets
from biscuits.serializers import *
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer