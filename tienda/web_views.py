from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from .models import Cliente, Pedido, Producto


@login_required
def dashboard(request):
    contexto = {
        "total_productos": Producto.objects.count(),
        "total_clientes": Cliente.objects.count(),
        "total_pedidos": Pedido.objects.count(),
    }
    return render(request, "tienda/dashboard.html", contexto)


class ProductoListaView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "tienda/productos_lista.html"
    context_object_name = "productos"
    ordering = ["nombre"]
    
    