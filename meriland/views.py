from django.shortcuts import render, get_object_or_404
from meriland.models import Post
from meriland.forms import ComentariosForm
from django.conf import settings
import requests


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def contacto(request):
    print("Entro")
    formset = ComentariosForm()

    if request.method == 'POST':
        print("Previo")
        form = ComentariosForm(request.POST)
        captcha_rs = form.get("g-recaptcha")
        print(form)
        print(captcha_rs)
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': captcha_rs,
            'remoteip': get_client_ip(request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        print(verify_rs.get("success", False))

        if form.is_valid():
            form.save()
            return render(request, "gracias.html", {})
        else:
            return render(request, "contacto.html", {"formset": formset})
    else:
        return render(request, "contacto.html", {"formset": formset})


def index(request):
    posts = Post.objects.filter(publicado=True, esnoticia=True).order_by('id').reverse()[:6]
    print(posts)
    return render(request, "index.html", {"posts": posts})


def post(request, slug):
    return render(request, "post.html", {
        "post": get_object_or_404(Post, slug=slug)
    })


def filtronoticia(request, clasificacion):
    posts = Post.objects.filter(publicado=True, clasificacion=clasificacion).order_by('id').reverse()[:6]
    return render(request, "index.html", {"posts": posts})


def todaslasnoticias(request):
    posts = Post.objects.filter(publicado=True, esnoticia=True).order_by('id').reverse()[:20]
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

