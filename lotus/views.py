from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


def home(request):
    latest_posts = models.Post.objects.all().order_by('-date_posted')
    if len(latest_posts) > 3:
        latest_posts = latest_posts[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'lotus/home.html', context)


def contact(request):
    return render(request, 'lotus/contact.html')


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
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


def subscription(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Email received. thank You! ")  # message

    return redirect("home")
