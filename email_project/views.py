import dotenv

dotenv.load_dotenv()

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(subject, message, settings.EMAIL_HOST_USER, [address])


    return render(request, "index.html", context)