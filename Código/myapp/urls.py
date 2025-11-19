from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("criar-lista/", views.criar_lista, name="criar_lista"),
    path("minhas-listas/", views.minhas_listas, name="minhas_listas"),
    path("lista/<int:id_lista>/", views.ver_lista, name="ver_lista"),
    path("lista/<int:id_lista>/add-item/", views.adicionar_item, name="adicionar_item"),
]
