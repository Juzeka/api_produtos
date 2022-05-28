from rest_framework.viewsets import ModelViewSet
from etapas.serializers import EtapaAllSerializer
from etapas.models import Etapa


class EtapaViewSet(ModelViewSet):
    queryset = Etapa.objects.all()
    serializer_class = EtapaAllSerializer