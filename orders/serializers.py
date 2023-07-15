from rest_framework import serializers

from comics.models import Comics
from mainapp.tasks import send_order_confirm_email
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        exclude = ('order_confirm', 'confirm_code')

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.create_confirm_code()
        order.save()
        send_order_confirm_email.delay(order.user.email, order.confirm_code)
        return order

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        comics = Comics.objects.get(id=repr['comics']).name
        repr['order_confirm'] = instance.order_confirm
        repr['comics'] = comics
        return repr

    def validate(self, attrs):
        comics = attrs['comics']
        count = attrs['count']
        if comics.amount < count:
            raise serializers.ValidationError(f'You cannot order this amount, there are only {comics.amount} in stock')
        return attrs

