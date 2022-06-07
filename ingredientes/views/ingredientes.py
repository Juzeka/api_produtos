from utils.viewset import ViewSetCustom
from ingredientes.serializers.ingredientes import IngredientesAllSerializers
from ingredientes.models.ingredientes import Ingrediente


class IngredientesViewSet(ViewSetCustom):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredientesAllSerializers