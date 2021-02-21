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
    posts = Post.objects.filter(publicado=True, esnoticia=True)[:9]
    print(posts)
    return render(request, "index.html", {"posts": posts})


def post(request, slug):
    return render(request, "post.html", {
        "post": get_object_or_404(Post, slug=slug)
    })


def filtronoticia(request, clasificacion):
    posts = Post.objects.filter(publicado=True, clasificacion=clasificacion)[:9]
    return render(request, "index.html", {"posts": posts})


def todaslasnoticias(request):
    posts = Post.objects.filter(publicado=True, esnoticia=True)[:20]
    return render(request, "index.html", {"posts": posts})


def quienessomos(request):
    return render(request, "quienessomos.html", {})


def avisoprivacidad(request):
    return render(request, "avisoprivacidad.html", {})


def dondeestamos(request):
    return render(request, "dondeestamos.html", {})


def desarrolladopor(request):
    return render(request, "desarrolladopor.html", {})


def captcha(request):
    return render(request, "captcha.html", {})

