from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CharacterCreateView.as_view()),
    path('list/', views.CharacterListView.as_view()),
    path('detail/<int:pk>/', views.CharacterRetrieveView.as_view()),
    path('update/<int:pk>/', views.CharacterUpdateView.as_view()),
    path('delete/<int:pk>/', views.CharacterDeleteView.as_view()),

]