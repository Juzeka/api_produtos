from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ingredientes.views.ingredientes import IngredientesViewSet
from etapas.views.etapas import EtapaViewSet


routers = DefaultRouter()
routers.register(r'ingredientes', IngredientesViewSet)
routers.register(r'etapas', EtapaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls), name='api'),
]
