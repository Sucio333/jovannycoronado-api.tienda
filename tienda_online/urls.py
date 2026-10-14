from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView

from tienda import web_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tienda.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="tienda/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", web_views.dashboard, name="dashboard"),
    path("productos/", web_views.ProductoListaView.as_view(), name="productos"),
    path("", TemplateView.as_view(template_name="tienda/index.html"), name="home"),
]