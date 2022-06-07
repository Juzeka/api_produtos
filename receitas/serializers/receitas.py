from rest_framework.serializers import ModelSerializer
from receitas.models import Receita
from ingredientes.serializers import IngredientesAllSerializers
from etapas.serializers import EtapaAllSerializer


class ReceitaAllSerializer(ModelSerializer):
    ingredientes = IngredientesAllSerializers(many=True, read_only=True)
    etapas = EtapaAllSerializer(many=True, read_only=True)


    class Meta:
        model = Receita
        fields = '__all__'


class ReceitaCreateUpdateSerializer(ReceitaAllSerializer):
    ingredientes = IngredientesAllSerializers(many=True, read_only=False)
    etapas = EtapaAllSerializer(many=True, read_only=False)