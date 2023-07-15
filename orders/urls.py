from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register('', views.OrderViewSet)

urlpatterns = [
    path('confirm/<uuid:confirm_code>/', views.OrderConfirmView.as_view()),
    path('list-create/', views.OrderView.as_view()),
    path('delete/<int:pk>/', views.OrderDeleteFromUserView.as_view()),

]