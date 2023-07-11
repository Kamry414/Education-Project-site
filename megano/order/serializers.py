from rest_framework import serializers
from .models import Order, BasketItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'createdAt', 'fullName', 'email', 'phone', 'deliveryType', 'paymentType', 'totalCost', 'status', 'city', 'address', 'products']



class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'images', 'tags', 'reviews', 'rating']
