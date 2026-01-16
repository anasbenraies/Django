from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='/users/login/')
def posts_list(request):
    posts = Post.objects.all().order_by("-created")
    return render(request, 'posts/posts_list.html', {'posts': posts})


@login_required(login_url='/users/login/')
def post_page(request , slug):
    """
    This view renders a page for a single post given its slug.

    It expects a GET request with a slug parameter, and renders
    the post_page.html template with the corresponding Post object.

    :param request: The HTTP request object.
    :param slug: The slug of the post to be rendered.
    :return: An HTTP response with the rendered page.
    """
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})
