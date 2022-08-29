from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Marca, Veiculo
from core.serializers import CategoriaSerializer, MarcaSerializer, VeiculoSerializer, VeiculoDetailSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return VeiculoDetailSerializer
        return VeiculoSerializer      