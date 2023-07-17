from rest_framework import serializers
from .models import OrderItem, Order
from comics.models import Comics


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source="product.name")

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'product_title')


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    products = OrderItemSerializer(write_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        print("Функция create начал работу я*********************************************")
        products = validated_data.pop('products')
        print(f'products = {products}')
        user = self.context['request'].user
        total_sum = 0
        for product in products:
            print(f'oneproduct = {product}')
            total_sum += product['quantity'] * product['product'].price
        order = Order.objects.create(user=user, total_sum=total_sum, status='open', **validated_data)
        print(f'order - {order}')
        order_item_objects = [OrderItem(order=order, product=product['product'], quantity=product['quantity'])
                              for product in products
                              ]
        print(f'order_item_objects - {order_item_objects}')
        print(f'TotalSum - {total_sum}')
        # разом создает много оъектов
        OrderItem.objects.bulk_create(order_item_objects)
        print("Функция create закончила свою раблту ****************************************")
        return order

    def to_representation(self, instance):
        print("функция to_represenation начала работу ****************************************")
        repr = super().to_representation(instance)
        print(f'repr - {repr}')
        repr['products'] = OrderItemSerializer(instance.items.all(), many=True)
        repr.pop('products')
        print('функция to_representation закончила работу -********************************************')
        return repr
