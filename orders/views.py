from rest_framework.response import Response

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from . import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class CreateOrderView(ListCreateAPIView):
    serializer_class =serializers.OrderSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        user = request.user
        order = user.order.all()
        serializer = serializers.OrderSerializer(order,many=True)
        return Response(serializer.data, status=200)
