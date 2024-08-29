from biscuits.models import *
from rest_framework import viewsets
from biscuits.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import api_view


class RegisterView(APIView):
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserProfileViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        if pk == 'me':
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        print("request.headers")
        if pk == 'me':
            user = request.user
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = UserDataSerializer(request.user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        user = request.user
        data = request.data

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.address = data.get('address', user.address)
        user.city = data.get('city', user.city)
        user.phone = data.get('phone', user.phone)
        user.postal = data.get('postal', user.postal)
        user.save()

        serializer = UserDataSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        raise MethodNotAllowed('POST')

    def destroy(self, request, pk=None):
        raise MethodNotAllowed('DELETE')

    def partial_update(self, request, pk=None):
        user = request.user
        data = request.data

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.address = data.get('address', user.address)
        user.city = data.get('city', user.city)
        user.phone = data.get('phone', user.phone)
        user.postal = data.get('postal', user.postal)
        user.save()

        serializer = UserDataSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = OrderSerializer(Order.objects.filter(owner=request.user),many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        raise MethodNotAllowed('PUT')

    def create(self, request):
        print(request.data)
        order = Order(uuid=request.data['uuid'], status=request.data['status'], owner=request.user)
        order.save()
        for element in request.data['elements']:
            order_element = OrderElement(quantity=element['quantity'], product=Product.objects.get(id=element['id']), related_order=order)
            order_element.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        raise MethodNotAllowed('DELETE')

    def partial_update(self, request, pk=None):
        raise MethodNotAllowed('PATCH')

@api_view(['GET'])
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)