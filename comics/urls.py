from django.urls import path, include
from rest_framework.routers import SimpleRouter

from comics.views import ComicsCreateView, ComicsListingView, ComicsUpdateView, ComicsDeleteView, ComicsDetailView

#
# from account.views import AccountViewSet, Login, Refresh

# router = SimpleRouter()
# router.register('', AccountViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('login/', Login.as_view()),
    # path('refresh/', Refresh.as_view()),
    path('create/', ComicsCreateView.as_view()),
    path('',ComicsListingView.as_view()),
    path('detail/<int:pk>/',ComicsDetailView.as_view()),
    path('update/<int:pk>/',ComicsUpdateView.as_view()),
    path('delete/<int:pk>/',ComicsDeleteView.as_view()),
    # path('comment/create/',CreateCommentView.as_view()),
]