from rest_framework.serializers import ModelSerializer
from ingredientes.models.ingredientes import Ingrediente


class IngredientesAllSerializers(ModelSerializer):
    class Meta:
        model =Ingrediente
        fields = '__all__'