from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def insert_email(request):
    send_mail('subject',
              'hiiiiii hellloooo namastey venikhaa singh',
              'yadavchandrika789@gmail.com',
              ['vvenikha@gmail.com'],
              fail_silently=False)
    return HttpResponse('success fully sended')