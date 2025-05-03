from rest_framework import serializers
from .models import User, Product, Order, OrderItem
from django.contrib.auth import get_user_model

# Import TokenObtainPairSerializer from SimpleJWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Import TokenObtainPairView for creating the custom token view
from rest_framework_simplejwt.views import TokenObtainPairView

# Get the user model
User = get_user_model()


# serializers.py
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        data['is_superuser'] = self.user.is_superuser
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'date_ordered', 'items']
