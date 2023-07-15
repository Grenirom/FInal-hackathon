from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        res = queryset.filter(user=user)
        return res


class OrderDeleteFromUserView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]



class OrderConfirmView(APIView):
    @staticmethod
    def get(request, confirm_code):
        try:
            order = Order.objects.get(confirm_code=confirm_code)
            order.order_confirm = True
            order.confirm_code = ''
            ordered_count = order.count
            comics = order.comics
            amount = comics.amount
            comics.amount = amount - ordered_count
            if comics.amount == 0:
                comics.STATUS = 'out_of_stock'
            comics.save()
            order.save()
            return Response({'msg': 'Order confirmed!'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'msg': 'Invalid order confirmation code'}, status=status.HTTP_400_BAD_REQUEST)
