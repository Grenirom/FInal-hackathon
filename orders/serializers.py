from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = OrderItem
        fields = ('movie', 'movie_title', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user_full_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'user_full_name', 'order_items', 'created_at', 'updated_at', 'total_amount', 'is_completed')
