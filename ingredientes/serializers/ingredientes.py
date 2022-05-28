from rest_framework.serializers import ModelSerializer
from ingredientes.models import Ingrediente


class IngredientesAllSerializers(ModelSerializer):
    class Meta:
        model =Ingrediente
        fields = '__all__'