from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from parsing.views import ParsingListAPIView
from mainapp import settings
from orders.views import CreateOrderView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      # contact=openapi.Contact(email="contact@snippets.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('category/', include('category.urls')),
    path('news/', include('news.urls')),
    path('movies/', include('movies.urls')),
    path('characters/', include('characters.urls')),
    path('comics/', include('comics.urls')),
    path('orders/', CreateOrderView.as_view()),
    path('parsing/',ParsingListAPIView.as_view()),
]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
