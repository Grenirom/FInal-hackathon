from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('', views.NewViewSet)


urlpatterns = [
    # path('list-create/', views.NewCreateListView.as_view()),
    # path('retr-upd-del/<int:pk>/', views.NewRetrieveUpdateDeleteView.as_view()),
    path('', include(router.urls)),
]