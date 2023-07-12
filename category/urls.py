from django.urls import path
from . import views

urlpatterns = [
    path('create-list/', views.CategoryCreateListView.as_view()),
    path('delete/<str:pk>/', views.CategoryDeleteView.as_view()),
]