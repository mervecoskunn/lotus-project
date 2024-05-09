from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    post_list = Post.objects.all()
    post_list.reverse()
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)
