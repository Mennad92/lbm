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

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'stock', 'illustration']

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