from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from comics.models import Comics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class ComicsCreateView(CreateAPIView):
    queryset = Comics.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name', )
    filterset_fields = ('name', 'price')
    serializer_class = serializers.ComicsSerializers
    permission_clbodyasses = [IsAdminUser, ]


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