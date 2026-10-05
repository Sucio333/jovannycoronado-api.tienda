from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaViewSet,
    ClienteViewSet,
    DetallePedidoViewSet,
    PedidoViewSet,
    ProductoViewSet,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"detalles-pedido", DetallePedidoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]