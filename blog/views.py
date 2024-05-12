from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def post_list(request):
    post_list = Post.objects.all().order_by('-date_posted')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('post_list')


@login_required
def post_confirm_delete(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_confirm_delete.html', context)


@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post edited successfully')
            return redirect('post_list')  # Redirect to the post list page
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post added successfully')
            return redirect('post_list')  # Redirect to the post list page
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
