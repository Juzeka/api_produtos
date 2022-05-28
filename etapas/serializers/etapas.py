from rest_framework.serializers import ModelSerializer
from etapas.models import Etapa


class EtapaAllSerializer(ModelSerializer):
    class Meta:
        model = Etapa
        fields = '__all__'