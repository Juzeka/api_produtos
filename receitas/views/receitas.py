from utils.viewset import ViewSetCustom
from receitas.serializers import (
    Receita, ReceitaAllSerializer, ReceitaCreateUpdateSerializer
)


class ReceitaViewSet(ViewSetCustom):
    queryset = Receita.objects.all()
    serializer_class = ReceitaAllSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            self.serializer_class = ReceitaCreateUpdateSerializer

        return super().get_serializer_class()