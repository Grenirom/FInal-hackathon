from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('create/', views.CharacterCreateView.as_view()),
    path('list/', cache_page(60 * 10)(views.CharacterListView.as_view())),
    path('detail/<int:pk>/', views.CharacterRetrieveView.as_view()),
    path('update/<int:pk>/', views.CharacterUpdateView.as_view()),
    path('delete/<int:pk>/', views.CharacterDeleteView.as_view()),

]