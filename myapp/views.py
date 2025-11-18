from django.shortcuts import render, redirect, get_object_or_404
from .models import Lista, Item, Categoria

def get_user_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def home(request):
    return render(request, "home.html")


def criar_lista(request):
    session = get_user_session(request)

    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")

        Lista.objects.create(
            session_key=session,
            nome=nome,
            descricao=descricao
        )
        return redirect("minhas_listas")

    return render(request, "criar_lista.html")


def minhas_listas(request):
    session = get_user_session(request)
    listas = Lista.objects.filter(session_key=session)
    return render(request, "minhas_listas.html", {"listas": listas})


def ver_lista(request, id_lista):
    lista = get_object_or_404(Lista, id=id_lista)
    categorias = Categoria.objects.all()
    return render(request, "ver_lista.html", {"lista": lista, "categorias": categorias})


def adicionar_item(request, id_lista):
    lista = get_object_or_404(Lista, id=id_lista)

    if request.method == "POST":
        nome = request.POST.get("nome")
        imagem = request.POST.get("imagem_url")
        link = request.POST.get("produto_url")
        categoria_id = request.POST.get("categoria")
        categoria = Categoria.objects.get(id=categoria_id)

        Item.objects.create(
            lista=lista,
            nome=nome,
            imagem_url=imagem,
            produto_url=link,
            categoria=categoria,
        )

        return redirect("ver_lista", id_lista=id_lista)

    categorias = Categoria.objects.all()
    return render(request, "adicionar_item.html", {"categorias": categorias})
