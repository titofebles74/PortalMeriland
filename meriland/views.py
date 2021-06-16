from django.shortcuts import render, get_object_or_404
from meriland.models import Post
from meriland.forms import ComentariosForm, CaptchForm
from django.conf import settings
import urllib
import urllib.request
import json


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def captcha(request):
    return render(request, "captcha.html", {})


def contacto(request):
    formset = ComentariosForm()

    if request.method == 'POST':
        ''' End reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_PUBLIC_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode("utf-8")
        req = urllib.request.urlopen(url, data)
        result = json.load(req)
        ''' End reCAPTCHA validation '''

        form = ComentariosForm(request.POST)
        if result['success'] == True:
            print(form)
            if form.is_valid():
                form.save()
                return render(request, "gracias.html", {})
            else:
                return render(request, "contacto.html", {"formset": form})
        else:
            return render(request, "error.html", {})
    else:
        return render(request, "contacto.html", {"formset": formset})


def index(request):
    posts = Post.objects.filter(publicado=True, esnoticia=True).order_by('id').reverse()[:6]
    return render(request, "index.html", {"posts": posts})


def post(request, slug):
    return render(request, "post.html", {
        "post": get_object_or_404(Post, slug=slug)
    })


def filtronoticia(request, clasificacion):
    posts = Post.objects.filter(publicado=True, clasificacion=clasificacion).order_by('id').reverse()[:6]
    return render(request, "index.html", {"posts": posts})


def todaslasnoticias(request):
    posts = Post.objects.filter(publicado=True, esnoticia=True).order_by('id').reverse()[:12]
    return render(request, "index.html", {"posts": posts})


def quienessomos(request):
    return render(request, "quienessomos.html", {})


def avisoprivacidad(request):
    return render(request, "avisoprivacidad.html", {})


def dondeestamos(request):
    return render(request, "dondeestamos.html", {})


def desarrolladopor(request):
    return render(request, "desarrolladopor.html", {})


def esquema(request):
    return render(request, "esquema.htm", {})


def codigoarduino(request):
    return render(request, "codigoarduino.htm", {})


def iothome(request):
    return render(request, "iot.htm", {})


def tupagina(request):
    return render(request, "tu_pagina.htm", {})

