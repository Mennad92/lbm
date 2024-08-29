from biscuits.models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'stock', 'illustration', 'ingredients']
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        product = Product.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
            product.ingredients.add(ingredient)
        return product

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.illustration = validated_data.get('illustration', instance.illustration)
        instance.save()

        instance.ingredients.clear()
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'])
            instance.ingredients.add(ingredient)

        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDataSerializer(serializers.ModelSerializer):

    class Meta :
        model = UserData
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    owner = UserDataSerializer()

    class Meta:
        model = Order
        fields = '__all__'