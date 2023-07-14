from django.core.paginator import Paginator
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from . import serializers
from .models import Movie


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', 'description')
    filterset_fields = ('category', 'price')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MovieListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.MovieCreateSerializer
        return serializers.MovieDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'delete', 'create'):
            return [permissions.AllowAny(), ]
        return [permissions.AllowAny(), ]


