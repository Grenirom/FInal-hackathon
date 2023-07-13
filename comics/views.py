from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import UpdateModelMixin
from comics.models import Comics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, \
    GenericAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters
# Create your views here.

class ComicsCreateView(CreateAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAdminUser, ]


# class CreateCommentView(CreateAPIView):
#     serializer_class = serializers.CreateCommentSerializer
#     permission_classes = [AllowAny, ]


class ComicsListingView(ListAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsListingSerializers
    permission_classes = [IsAuthenticated,]
    filter_backends = (DjangoFilterBackend,)



class ComicsDetailView(RetrieveAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAuthenticated,]

class ComicsUpdateView(UpdateAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAdminUser, ]
    # lookup_field = "id"


class ComicsDeleteView(DestroyAPIView):
    queryset = Comics.objects.all()
    serializer_class = serializers.ComicsSerializers
    permission_classes = [IsAdminUser, ]