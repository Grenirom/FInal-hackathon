from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import New
from .serializers import NewListSerializer, NewCreateSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class NewCreateListView(generics.ListCreateAPIView):
    queryset = New.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title',)
    filterset_fields = ('category',)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        else:
            return [permissions.IsAdminUser(), ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return NewListSerializer
        else:
            return NewCreateSerializer


class NewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewCreateSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        elif self.request.method in ('PUT', 'PATCH'):
            return [permissions.IsAdminUser(), ]
        else:
            return [permissions.IsAdminUser(), ]

