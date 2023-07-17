from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from comics.models import Comics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView


class ComicsCreateView(CreateAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAdminUser, ]


class ComicsListingView(ListAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsListingSerializers
    permission_classes = [IsAuthenticated,]
    filter_backends = (DjangoFilterBackend,)


class ComicsDetailView(RetrieveAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [AllowAny,]


class ComicsUpdateView(UpdateAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAdminUser, ]


class ComicsDeleteView(DestroyAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAdminUser, ]