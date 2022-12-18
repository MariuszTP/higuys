from django.shortcuts import render
from pageb.models import *
from django.db import models

from django.http import HttpResponse

from django.core.mail import send_mail, BadHeaderError

from django.contrib import messages

# Create your views here.


def base(request):
    return render(request, 'base1.html')

def main1(request):
    return render(request, 'index1.html')

def main2(request):
    return render(request, 'index2.html')

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


    return render(request, 'index1.html')





def opinion(request):
    if request.method =="POST":
        message = request.POST.get("opinion")
        print(message)    
        if len(message) > 20:
            messages.warning(request,'Teks zbyt długi, max limit 2000 znaków')
            return render(request, 'about.html')
        else:
            wiadomosc = Opinion(name=message)
            wiadomosc.save()
            messages.success(request,'wiadomosc wysłana')
    return render(request, 'index1.html')


def gallery1(request):
    products = Gallery1.objects.all()
    context = {'products': products}
    return render(request, 'gallery1.html', context)

def gallery2(request):
    return render(request, 'gallery2.html')

def gallery3(request):
    products = Image3.objects.all()
    context = {'products': products}
    return render(request, 'gallery3.html', context)

def gallery4(request):
    products = Image3.objects.all()
    context = {'products': products}
    return render(request, 'gallery4.html', context)

def gallery5(request):
    products = Image3.objects.all()
    context = {'products': products}
    return render(request, 'gallery5.html', context)


def materialy(request):
    kategoria = Kategoria.objects.all()
    kategory_id = request.GET.get('kategoria')
    if kategory_id:
        products = Gallery1.objects.filter(kategoria=kategory_id)
    else:
        products = Gallery1.objects.all()
    context = {'products': products, 'kategoria': kategoria}
    return render(request, 'materialy.html', context)

def about(request):
    return render(request, 'about.html')

def opinie(request):
    queryset = Opinion.objects.filter(approval=True)
    context = {'queryset': queryset}

    return render(request, 'opinion.html', context)

