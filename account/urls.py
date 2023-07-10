from django.urls import path, include
from rest_framework.routers import SimpleRouter

from account.views import AccountViewSet, Login, Refresh

router = SimpleRouter()
router.register('', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view()),
    path('refresh/', Refresh.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]