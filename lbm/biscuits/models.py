from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=70)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Role(models.Model):
    nom = models.CharField(max_length=70)
    permission = models.CharField(max_length=255)

    def definir_permission(self, nouvelle_permission):
        self.permission = nouvelle_permission
        self.save()

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=70)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    illustration = models.TextField()

    def __str__(self):
        return self.nom

class Compte(AbstractUser):
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Panier(models.Model):
    user = models.ForeignKey(Compte, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)

    def __str__(self):
        return f"Panier de {self.user.username}"

class Livraison(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=50)

    def livrer_commande(self, commande):
        self.statut = "livrée"
        self.save


    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut
        self.save()

    def __str__(self):
        return f"Transaction {self.id} - Statut: {self.statut}"
    
    class Meta:
        verbose_name = "Livraison"
        verbose_name_plural = "Livraisons"