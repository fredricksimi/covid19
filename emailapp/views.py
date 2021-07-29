from django.http.request import RawPostDataException
from django.shortcuts import render
from covid19.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcom to Potato'
        message = ''
        recipient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        return render(request, 'emailapp/successful.html', {'recepient':recipient})
    return render(request, 'emailapp/index.html', {'emailform':sub})
