from rest_framework.serializers import ModelSerializer
from receitas.models import Receita


class ReceitaAllSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'