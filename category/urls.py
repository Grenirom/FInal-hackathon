from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('create-list/', cache_page(60 * 10)(views.CategoryCreateListView.as_view())),
    path('delete/<str:pk>/', views.CategoryDeleteView.as_view()),
]