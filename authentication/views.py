from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from user.models import Profile
from . import forms
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # Check if user exists
        if user is not None:
            auth_login(request, user)
            m = f'You have been logged in as {user.username}'
            messages.success(request, m)
            return redirect('home')
        else:
            user = get_user_model().objects.filter(username=username).first()
            if user is not None and not user.is_active:
                m = 'Account is not activated. '
                m += 'Please check your email for activation link.'
                messages.error(request, m)
            else:
                messages.error(request, 'Username or password is incorrect.')

    return render(request, 'authentication/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'authentication/register.html')
        else:
            new_user = get_user_model().objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                # Hash the password before saving
                password=make_password(password)
            )
            new_user.is_active = False
            new_user.save()
            if new_user:
                # Create a Profile associated with the newly created User
                Profile.objects.create(user=new_user, address=address).save()

            # Send activation email
            html_content = render_to_string(
                template_name='authentication/activate_email.html',
                context={
                    'user': new_user.username,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                    'token': account_activation_token.make_token(new_user),
                    "protocol": "https://" if request.is_secure() else "http://",
                }
            )
            plain_message = strip_tags(html_content)

            send_mail(
                subject='Activation Link',
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                html_message=html_content,
                fail_silently=True
            )

            messages.success(request, 'Account was created for ' +
                             email + '. Please activate your account.')
        return redirect('login')

    return render(request, 'authentication/register.html', )


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except Exception as e:
        print("Mail send error: ", e)
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid.')
        return redirect('login')


@login_required
def change_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = request.user
        user.email = email
        user.is_active = False
        user.save()

        # Send activation email
        mail_subject = 'Activation link has been sent to your email id'
        html_content = render_to_string(
            template_name='authentication/activate_email.html',
            context={
                'user': user.username,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                "protocol": "https://" if request.is_secure() else "http://",
            }
        )
        plain_message = strip_tags(html_content)

        send_mail(
            subject=mail_subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_content,
            fail_silently=True
        )

        m = 'Email changed successfully. '
        m += 'Please check your email for activation link.'
        messages.success(request, m)
        auth_logout(request)
        return redirect('login')
    return render(request, 'authentication/change_email.html')


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'authentication/login.html')


class CustomPasswordResetView(PasswordResetView):
    form_class = forms.CustomPasswordResetForm
    template_name = "authentication/password_reset.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = forms.CustomSetPasswordForm
    template_name = "authentication/password_reset_confirm.html"
