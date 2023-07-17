from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from . import utils

# LIKE----------------------------------------------------------------------------------------------------------


class LikeMixin:
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        status_ = utils.like_unlike(user=user, obj=obj)
        return Response({'status': status_, 'user': user.email}, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        return Response(utils.get_fans(obj=obj), status=status.HTTP_200_OK)

# RATING---------------------------------------------------------------------------------------------


class RatingMixin:
    @action(methods=['POST'], detail=True)
    def add_rating(self, request, pk=None):
        try:
            obj = self.get_object()
            user = request.user
            rating = request.data['rating']
            status_ = utils.add_rating(obj=obj, user=user, rating=rating)
            return Response({'status': status_, 'user': user.email, 'rating': rating}, status=status.HTTP_200_OK)
        except:
            return Response('Rating Field Is Required!')

    @action(methods=['POST'], detail=True)
    def delete_rating(self, request, pk=None):
        user = request.user
        obj = self.get_object()
        utils.delete_rating(user=user, obj=obj)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=True)
    def reviewers(self, request, pk=None):
        obj = self.get_object()
        user_data = utils.get_rates(obj=obj)
        return Response(user_data, status=status.HTTP_200_OK)

# COMMENTS--------------------------------------------------------------------------------------------------------


class CommentMixin:
    @action(methods=['POST'], detail=True)
    #Добавление комментария
    def add_comment(self, request, pk=None):
        try:
            comment = request.data['comment']
            user = request.user
            obj = self.get_object()
            status_ = utils.add_comment(user=user, obj=obj, comment=comment)
            return Response(
                {
                    'status': status_,
                    'user': user.email,
                    'comment': comment,
                }, status=status.HTTP_200_OK
            )
        except:
            return Response('Comment field is required!')

    @action(methods=['POST'], detail=True)
    # Удаление комментария
    def delete_comment(self, request, pk=None):
        user = request.user
        obj = self.get_object()
        utils.delete_comment(obj=obj, user=user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(['GET'], detail=True)
    # Получение всех юзеров которые комментили
    def get_commenters(self, request, pk=None):
        return Response(utils.get_commenters(obj=self.get_object()), status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    # Получение всех комментов юзера
    def get_comments(self, request, pk=None):
        try:
            return Response(utils.get_user_comments(user=request.user), status=status.HTTP_200_OK)
        except TypeError:
            return Response({'msg': 'You aren\'t authorized!'}, status=status.HTTP_400_BAD_REQUEST)


# FAVORITES-------------------------------------------------------------------------------------------------


class FavoriteMixin:
    @action(methods=['POST'], detail=True)
    def favorites(self, request, pk=None):
        obj = self.get_object()
        user = request.user
        status_ = utils.add_or_delete_favorite(user=user, obj=obj)
        return Response(
            {
                'status': status_,
                'user': user.email,
                'new': obj.title,
            },
            status=status.HTTP_200_OK
        )

    @action(methods=['GET'], detail=False)
    def get_favorites(self, request):
        new_data = utils.get_favorites(user=request.user)
        return Response(new_data, status=status.HTTP_200_OK)


