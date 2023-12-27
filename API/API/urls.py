from django.contrib import admin
from django.urls import path, include
from ApiApp.views import TrabajadorViewSet, ProductoViewSet, CantidadPeliculasPorCategoriaView, PeliculaViewSet, TiendaViewSet ,IngresosArriendoPorTiendaView, ReparacionViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ApiApp/', include('ApiApp.urls')),
    path('api/trabajadores/', TrabajadorViewSet.as_view({'get': 'list', 'post': 'create'}), name='trabajadores-list-create'),
    path('api/trabajadores/<int:pk>/', TrabajadorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='trabajadores-detail'),
    path('api/productos/', ProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='Producto-list-create'),
    path('api/productos/<int:pk>/', ProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='producto-detail'),
    path('api/peliculas/', PeliculaViewSet.as_view({'get': 'list', 'post': 'create'}), name='Pelicula-list-create'),
    path('api/peliculas/<int:pk>/', PeliculaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='pelicula-detail'),
    path('cantidad_peliculas_por_categoria/', CantidadPeliculasPorCategoriaView.as_view(), name='cantidad_peliculas_por_categoria'),
    path('api/ingresos_arriendo_por_tienda/', IngresosArriendoPorTiendaView.as_view(), name='ingresos_arriendo_por_tienda'),
    path('api/tiendas/', TiendaViewSet.as_view({'get': 'list', 'post': 'create'}), name='Tienda-list-create'),
    path('api/tiendas/<int:pk>/', TiendaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='reparacion-detail'),
    path('api/reparaciones/', ReparacionViewSet.as_view({'get': 'list', 'post': 'create'}), name='Reparacion-list-create'),
    path('api/reparaciones/<int:pk>/', ReparacionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='reparacion-detail'),
]
