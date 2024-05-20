from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from .models import Post, Newsletter
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
    prev_page = request.META.get('HTTP_REFERER', '/')

    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
        'prev_page': prev_page
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
            post = form.save()
            messages.success(request, 'Post added successfully')
            send_email_to_subscribers(request, post)
            return redirect('post_list')  # Redirect to the post list page
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
