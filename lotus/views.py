from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from blog import models
from django.contrib import messages
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home(request):
    latest_posts = models.Post.objects.all().order_by('-date_posted')
    if len(latest_posts) > 3:
        latest_posts = latest_posts[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'lotus/home.html', context)


def privacy_policy(request):
    return render(request, 'lotus/privacy-policy.html')


def faq(request):
    return render(request, 'lotus/faq.html')


def custom_500(request):
    return render(request, '500.html')


api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        # print("response: {}".format(response))
        return True
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        return False


def subscription(request):
    if request.method == "POST":
        email = request.POST.get('email')

        if not subscribe(email):  # function to access mailchimp
            messages.error(request, "Email alredy subscribed.")
            return redirect("home")

        # Send email to user
        html_content = render_to_string(
            template_name="lotus/subscription_email.html",
            context={
                'domain': get_current_site(request).domain,
                "protocol": "https" if request.is_secure() else "http",
            }
        )
        plain_message = strip_tags(html_content)

        send_mail(
            subject='Newsletter Subscription',
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            html_message=html_content,
            fail_silently=True
        )

        models.Newsletter.objects.create(email=email).save()

        messages.success(request, "Subscription successfull. Thank You! ")

    return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email').strip()
        message = request.POST.get('message')
        # Get contact email
        html_content = render_to_string(
            template_name="lotus/contact_email.html",
            context={
                'name': name,
                'email': email,
                'message': message,
                "protocol": "https" if request.is_secure() else "http",
            }
        )
        plain_message = strip_tags(html_content)

        send_mail_return = send_mail(
            subject='New Contact Message',
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            html_message=html_content,
            fail_silently=True
        )

        contact = models.Contact.objects.create(
            name=name, email=email, message=message)
        contact.save()

        messages.success(request, "Your message has been sent successfully!")
    return render(request, 'lotus/contact.html')
