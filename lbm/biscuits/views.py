from biscuits.models import *
from rest_framework import permissions, viewsets

from biscuits.serializers import *


class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer