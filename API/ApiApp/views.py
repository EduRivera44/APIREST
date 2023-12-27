from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .models import Trabajador, Producto, Categoria, Pelicula, Tienda, Reparacion
from .serializers import TrabajadorSerializer, ProductoSerializer,CategoriaSerializer , PeliculaSerializer, TiendaSerializer, ReparacionSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

    def perform_create(self, serializer):
        categoria_id = self.request.data.get('categoria')
        categoria = Categoria.objects.get(pk=categoria_id)
        serializer.save(categoria=categoria)

class CantidadPeliculasPorCategoriaView(views.APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        data = []

        for categoria in categorias:
            cantidad_peliculas = Pelicula.objects.filter(categoria=categoria).count()
            data.append({
                'categoria': CategoriaSerializer(categoria).data,
                'cantidad_peliculas': cantidad_peliculas
            })

        return Response(data, status=status.HTTP_200_OK)
    
class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class IngresosArriendoPorTiendaView(views.APIView):
    def get(self, request):
        tiendas = Tienda.objects.all()
        data = []

        for tienda in tiendas:
            data.append({
                'tienda': TiendaSerializer(tienda).data,
                'ingresos_arriendo': tienda.ingresos_arriendo
            })

        return Response(data, status=status.HTTP_200_OK)
    
class ReparacionViewSet(viewsets.ModelViewSet):
    queryset = Reparacion.objects.all()
    serializer_class = ReparacionSerializer

