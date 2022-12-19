from django.shortcuts import render
from pageb.models import *
from django.db import models

from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError

from django.contrib import messages

# Create your views here.



def main(request):
    if request.method =="POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        from_email = request.POST.get("from_email")
        data = {
            'subject' : subject,
            'message' : message,
            'from_email' : from_email,
        }
        message = '''
        New message:{}
        From: {}
        '''.format(data['message'], data['from_email'])
        send_mail(data['subject'], message, '', ['turekpython@gmail.com'])
    return render(request, 'index.html')

def opinion(request):
    if request.method =="POST":
        message = request.POST.get("opinion")
        if len(message) > 2000:
            messages.warning(request,'Teks zbyt długi, max limit 2000 znaków')
            return render(request, 'index.html')
        else:
            wiadomosc = Opinion(text=message)
            wiadomosc.save()
            messages.success(request,'wiadomosc wysłana')
    return render(request, 'index.html')

def materialy(request):
    categories = Category.objects.all()
    category_id = request.GET.get('cat')
    if category_id:
        products = Gallery.objects.filter(category = category_id)
    else:
        products = Gallery.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'materialy.html', context)

def about(request):
    return render(request, 'about.html')

def opinie(request):
    queryset = Opinion.objects.filter(approval=True)
    context = {'queryset': queryset}
    return render(request, 'opinion.html', context)

