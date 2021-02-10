from django.shortcuts import render, get_object_or_404
from meriland.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post(request, slug):
    return render(request, "post.html", {
        "post": get_object_or_404(Post, slug=slug)
    })


def contacto(request):
    return render(request, "contacto.html", {})

