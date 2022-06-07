from rest_framework.viewsets import ModelViewSet
from ingredientes.serializers.ingredientes import IngredientesAllSerializers
from ingredientes.models.ingredientes import Ingrediente
from rest_framework.authentication import (
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated


class IngredientesViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ingrediente.objects.all()
    serializer_class = IngredientesAllSerializers

