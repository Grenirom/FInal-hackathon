from django.urls import path

from comics.views import ComicsCreateView, ComicsListingView, ComicsUpdateView, ComicsDeleteView, ComicsDetailView


urlpatterns = [
    path('create/', ComicsCreateView.as_view()),
    path('', ComicsListingView.as_view()),
    path('detail/<int:pk>/', ComicsDetailView.as_view()),
    path('update/<int:pk>/', ComicsUpdateView.as_view()),
    path('delete/<int:pk>/', ComicsDeleteView.as_view()),
]