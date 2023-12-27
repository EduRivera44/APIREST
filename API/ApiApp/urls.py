from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrabajadorViewSet, ProductoViewSet, PeliculaViewSet, TiendaViewSet, IngresosArriendoPorTiendaView, ReparacionViewSet

router = DefaultRouter()
router.register(r'trabajadores', TrabajadorViewSet, basename='trabajadores')

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='productos')

router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet, basename='peliculas')

router = DefaultRouter()
router.register(r'tiendas', TiendaViewSet, basename='tiendas')

router = DefaultRouter()
router.register(r'reparaciones', ReparacionViewSet, basename='reparaciones')

urlpatterns = [
    path('api/', include(router.urls)),
    
]

