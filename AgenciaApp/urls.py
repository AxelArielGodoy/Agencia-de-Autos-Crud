from django.urls import path
from .views import index, crear_auto, buscar_auto, sobre_nosotros, blog, editar_auto, eliminar_auto

urlpatterns = [
    path("", index, name="index"),
    path("crearauto/", crear_auto, name="crear_auto"),
    path("buscarauto/", buscar_auto, name="buscar_auto"),
    path("sobrenosotros/", sobre_nosotros, name="sobre_nosotros"),
    path("blog/", blog, name="blog"),
    path("editarauto/<int:id>/", editar_auto, name="editar_auto"),
    path("eliminarauto/<int:id>/", eliminar_auto, name="eliminar_auto"),
]