from rest_framework.viewsets import ModelViewSet
from ingredientes.serializers.ingredientes import IngredientesAllSerializers
from ingredientes.models.ingredientes import Ingrediente
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IngredientesViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Ingrediente.objects.all()
    serializer_class = IngredientesAllSerializers

