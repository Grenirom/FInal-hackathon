from django.urls import path

from . import views


urlpatterns = [
    path('confirm/<uuid:confirm_code>/', views.OrderConfirmView.as_view()),
    path('list-create/', views.OrderView.as_view()),
    path('delete/<int:pk>/', views.OrderDeleteFromUserView.as_view()),
]
