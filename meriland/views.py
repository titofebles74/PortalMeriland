from django.shortcuts import render, get_object_or_404
from meriland.models import Post
from meriland.forms import ComentariosForm


def contacto(request):
    print("Entro")
    formset = ComentariosForm()

    if request.method == 'POST':
        print("Previo")
        form = ComentariosForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, "gracias.html", {})
        else:
            return render(request, "contacto.html", {"formset": formset})
    else:
        return render(request, "contacto.html", {"formset": formset})



def index(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, "index.html", {"posts": posts})


def post(request, slug):
    return render(request, "post.html", {
        "post": get_object_or_404(Post, slug=slug)
    })


def filtronoticia(request, clasificacion):
    posts = Post.objects.filter(clasificacion=clasificacion)
    return render(request, "index.html", {"posts": posts})


def quienessomos(request):
    return render(request, "quienessomos.html", {})


def avisoprivacidad(request):
    return render(request, "avisoprivacidad.html", {})

