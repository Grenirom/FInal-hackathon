from rest_framework import generics
from rest_framework import permissions
from .models import New
from .serializers import NewListSerializer, NewCreateSerializer


class NewCreateListView(generics.ListCreateAPIView):
    queryset = New.objects.all()

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

