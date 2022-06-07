from rest_framework.viewsets import ModelViewSet
from etapas.serializers import EtapaAllSerializer
from etapas.models import Etapa
from rest_framework.authentication import (
    TokenAuthentication
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class EtapaViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Etapa.objects.all()
    serializer_class = EtapaAllSerializer