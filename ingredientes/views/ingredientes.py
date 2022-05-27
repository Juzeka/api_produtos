from rest_framework.viewsets import ModelViewSet
from ingredientes.serializers.ingredientes import IngredientesAllSerializers
from ingredientes.models.ingredientes import Ingrediente


class IngredientesViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredientesAllSerializers

