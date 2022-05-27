from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from ingredientes.views.ingredientes import IngredientesViewSet
from etapas.views.etapas import EtapaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API de Receitas",
      default_version='v1',
      description="Descrição da api",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


routers = DefaultRouter()
routers.register(r'ingredientes', IngredientesViewSet)
routers.register(r'etapas', EtapaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls), name='api'),
]
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]