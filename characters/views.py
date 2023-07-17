from . import serializers
from rest_framework import generics, permissions
from .models import Character


class CharacterCreateView(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    permission_classes = (permissions.IsAdminUser,)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterListSerializer
    permission_classes = (permissions.AllowAny,)


class CharacterRetrieveView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    permission_classes = (permissions.AllowAny,)


class CharacterUpdateView(generics.UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    permission_classes = (permissions.IsAdminUser,)


class CharacterDeleteView(generics.DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer
    permission_classes = (permissions.IsAdminUser,)


def parse():
    main()