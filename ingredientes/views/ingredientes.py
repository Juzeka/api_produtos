from rest_framework.viewsets import ModelViewSet
from ingredientes.serializers.ingredientes import IngredientesAllSerializers
from ingredientes.models.ingredientes import Ingrediente
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class IngredientesViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredientesAllSerializers

    @permission_classes([AllowAny])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @permission_classes([AllowAny])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @permission_classes([AllowAny])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @permission_classes([IsAuthenticated])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @permission_classes([IsAdminUser])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)