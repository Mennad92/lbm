from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Category(models.Model):
    name = models.CharField(max_length=70)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    illustration = models.ImageField(upload_to='products/')
    ingredients = models.ManyToManyField(Ingredient, related_name="products")

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):

    username = None
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    postal =  models.CharField(max_length=10, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_data_set',
        blank=True,
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_data_permission_set',
        blank=True,
        verbose_name=('user permissions'),
    )


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Order(models.Model):
    WAITING_FOR_PAYMENT = 'En attente de paiement'
    EN_ATTENTE_DEXPEDITION = "En attente d'expedition"
    IN_DELIVERY = 'En cours de livraison'
    DELIVERED = 'Livré'
    CANCELLED = 'Annulé'

    STATUS_CHOICES = [
        (WAITING_FOR_PAYMENT, 'Waiting for Payment'),
        (EN_ATTENTE_DEXPEDITION, 'Waiting for Expedition'),
        (IN_DELIVERY, 'In Delivery'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    uuid = models.CharField(max_length=50,unique=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=WAITING_FOR_PAYMENT,
    )
    owner = models.ForeignKey(UserData, on_delete=models.CASCADE)

    def __str__(self):
        return f"Commande {self.uuid} pour {self.owner.first_name} {self.owner.last_name} - Statut: {self.status}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

class OrderElement(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    related_order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Element de commande {self.id} - {self.quantity} {self.product.name}"
    
    class Meta:
        verbose_name = "OrderElement"
        verbose_name_plural = "OrderElements"
