from rest_framework import serializers

from parsing.models import ParsingModel


class ParsingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParsingModel
        exclude = ('id',)