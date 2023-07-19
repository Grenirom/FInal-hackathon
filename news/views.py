from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .mixins import FavoriteMixin, LikeMixin, CommentMixin, RatingMixin
from .models import New
from .serializers import NewSerializer, NewCreateSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class NewViewSet(ModelViewSet, FavoriteMixin, CommentMixin, RatingMixin, LikeMixin):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title',)
    filterset_fields = ('category',)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), ]
        elif self.request.method == 'GET':
            return [permissions.AllowAny(), ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NewCreateView(generics.CreateAPIView):
    # queryset = New.objects.all()
    serializer_class = NewCreateSerializer
    permission_classes = [IsAdminUser, ]