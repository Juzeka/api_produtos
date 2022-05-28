from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from ingredientes.views import IngredientesViewSet
from etapas.views import EtapaViewSet
from receitas.views import ReceitaViewSet
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
   permission_classes=[permissions.IsAuthenticated],
)


routers = DefaultRouter()
routers.register(r'ingrediente', IngredientesViewSet)
routers.register(r'etapa', EtapaViewSet)
routers.register(r'receita', ReceitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls), name='api'),
]
urlpatterns += [
    re_path(r'^documentacao(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^documentacao/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]