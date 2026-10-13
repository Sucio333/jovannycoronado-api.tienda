from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Cliente, Pedido, Producto


@login_required
def dashboard(request):
    contexto = {
        "total_productos": Producto.objects.count(),
        "total_clientes": Cliente.objects.count(),
        "total_pedidos": Pedido.objects.count(),
    }
    return render(request, "tienda/dashboard.html", contexto)