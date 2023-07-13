from rest_framework import serializers
from category.models import Category
from .models import Movie, MovieImage


class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        if len(obj.description) > 30:
            return obj.description[:30] + '...'
        return obj.description

    class Meta:
        model = Movie
        fields = ('id', 'title', 'category', 'category_name', 'preview', 'description', 'release_date')


class MovieDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    images = MovieImageSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Movie
        fields = '__all__'
