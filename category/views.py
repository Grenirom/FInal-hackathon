from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        elif self.request.method == 'POST':
            return [permissions.IsAdminUser(), ]


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, ]