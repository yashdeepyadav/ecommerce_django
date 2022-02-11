from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from store.models import Category, Product, Order, OrderItem, Customer

class ProductSerializer(ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model= OrderItem
        fields= '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model= Order
        fields= '__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'