from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
from posts.models import Post


def hello_world(request):
    posts = Post.objects.all().order_by("-created-at")
    return render(
        request=request, 
        template_name="posts/hello.html", 
        content={
            "posts": posts
        }
    )