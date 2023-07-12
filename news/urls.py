from django.urls import path
from . import views


urlpatterns = [
    path('list-create/', views.NewCreateListView.as_view()),
    path('retr-upd-del/<int:pk>/', views.NewRetrieveUpdateDeleteView.as_view()),
]