from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.shortcuts import render, redirect, get_object_or_404

from . import forms
from .models import Post, Newsletter, DraftPost, Comment
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site


def post_list(request):
    post_list = Post.objects.all().order_by('-date_posted')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    if request.method == 'GET':
        prev_page = request.META.get('HTTP_REFERER', '/')

        post = Post.objects.get(pk=pk)
        liked = post.like.filter(id=request.user.id).exists()

        form = forms.CommentCreateForm()
        context = {
            'post': post,
            'prev_page': prev_page,
            'liked': liked,
            'comment_form': form
        }
        return render(request, 'blog/post_detail.html', context)
    elif request.method == 'POST':
        form = forms.CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = pk
            comment.save()
            return redirect(reverse('post_detail', args=[pk]))


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


def send_email_to_subscribers(request, post):
    """
    Sends an email to all subscribers
    """
    recipient_list = [
        subscriber.email for subscriber in Newsletter.objects.all()]

    html_content = render_to_string(
        template_name="blog/post_email.html",
        context={
            'domain': get_current_site(request).domain,
            "protocol": "https" if request.is_secure() else "http",
            "post_id": post.id,
        }
    )
    plain_message = strip_tags(html_content)

    send_mail(
        subject='New Post Alert',
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        html_message=html_content,
        fail_silently=True
    )


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if 'save_as_draft' in request.POST:
                # Save as draft
                draft_post = DraftPost(
                    img=form.cleaned_data['img'],
                    title=form.cleaned_data['title'],
                    content=form.cleaned_data['content']
                )
                draft_post.save()
                # Redirect to the list of draft posts or
                # any other appropriate page
                return redirect('draft_post_list')
            else:
                form.instance.author = request.user
                post = form.save()
                messages.success(request, 'Post added successfully')
                send_email_to_subscribers(request, post)
                return redirect('post_list')  # Redirect to the post list page
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


@login_required
def draft_post_list(request):
    draft_post_list = DraftPost.objects.all()
    context = {
        'draft_post_list': draft_post_list
    }
    return render(request, 'blog/draft_post_list.html', context)


@login_required
def draft_post_detail(request, pk):
    draft_post = DraftPost.objects.get(pk=pk)
    prev_page = request.META.get('HTTP_REFERER', '/')
    context = {
        'post': draft_post,
        'prev_page': prev_page
    }
    return render(request, 'blog/draft_post_detail.html', context)


@login_required
def draft_post_edit(request, pk):
    draft_post = DraftPost.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=draft_post)
        if form.is_valid():
            draft_post = form.save(commit=False)
            post = Post.objects.create(
                img=draft_post.img,
                title=draft_post.title,
                content=draft_post.content,
                author=request.user
            )
            post.save()
            draft_post.delete()
            messages.success(request, 'Draft post finished successfully')
            send_email_to_subscribers(request, post)
            return redirect('draft_post_list')

    else:
        form = PostForm(instance=draft_post)
    return render(request, 'blog/draft_post_edit.html', {'form': form})


@login_required
def draft_post_delete(request, pk):
    draft_post = DraftPost.objects.get(pk=pk)
    draft_post.delete()
    messages.success(request, 'Draft post deleted successfully')
    return redirect('draft_post_list')


@login_required
def draft_post_confirm_delete(request, pk):
    draft_post = DraftPost.objects.get(pk=pk)
    context = {
        'post': draft_post
    }
    return render(request, 'blog/draft_post_confirm_delete.html', context)


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))


def comment_edit(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    prev_page = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        form = forms.CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post_id = post_id
            form.save()
            messages.success(request, 'Comment update successful')
            return redirect(reverse('post_detail', args=[post_id]))
    else:
        form = forms.CommentEditForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form, 'prev_page': prev_page})


def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment delete successful')
        return redirect(reverse('post_detail', args=[post_id]))
    return redirect(reverse('post_detail', args=[post_id]))
