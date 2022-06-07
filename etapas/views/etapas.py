from utils.viewset import ViewSetCustom
from etapas.serializers import EtapaAllSerializer
from etapas.models import Etapa


class EtapaViewSet(ViewSetCustom):
    queryset = Etapa.objects.all()
    serializer_class = EtapaAllSerializer