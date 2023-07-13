from rest_framework import serializers

from comics.models import Comics  # , Comments
from rating.models import Rating
from rating.serializers import RatingSerializer


class ComicsSerializers(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Comics
        fields = ('id', 'name', 'published_at', 'author', 'cover_artist', 'description', 'artist', 'image', 'price',
                  'amount_of_pages', 'category', 'average_rating','ratings')

    def to_representation(self, instance):
        repr = super(ComicsSerializers, self).to_representation(instance)
        user = self.context['request'].user
        data = repr.pop('ratings')
        print(data,'******************************************************************************')
        marks = [item['mark'] for item in data]
        average = sum(marks) / len(marks)
        average = round(average, 1)
        repr['average_rating'] = average
        return repr


class ComicsListingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('id', 'name', 'image', 'price', 'amount_of_pages')

# class CreateCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comments
#         fields = "__all__"

