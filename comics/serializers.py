from rest_framework import serializers

from comics.models import Comics  # , Comments


class ComicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('id', 'name', 'published_at', 'author', 'cover_artist', 'description', 'artist', 'image', 'price',
                  'amount_of_pages', 'category')


class ComicsListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('id', 'name', 'image', 'price', 'amount_of_pages')

# class CreateCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comments
#         fields = "__all__"

