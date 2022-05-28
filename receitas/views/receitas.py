from rest_framework.viewsets import ModelViewSet
from receitas.serializers import Receita, ReceitaAllSerializer


class ReceitaViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaAllSerializer