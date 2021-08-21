from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.db.models import F

from core.models import Services, Doctors, News, AboutUs, Advices, Contacts, Address, Feedback, Products


def index(request):
    doctors = Doctors.objects.all()
    news = News.objects.all()
    service = Services.objects.all()
    about_us = AboutUs.objects.all()
    advice = Advices.objects.all()
    contacts = Contacts.objects.all()
    address = Address.objects.all()
    products = Products.objects.all()
    context = {
        'doctors': doctors,
        'news': news,
        'service': service,
        'about_us': about_us,
        'advice': advice,
        'contacts': contacts,
        'address': address,
        'products': products,

    }
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        area = request.POST['area']
        feedback = Feedback(fullname=fullname, area=area, email=email, phone_number=phone_number)
        feedback.save()
        return render(request, 'index.html', context)
    else:
        return render(request, "index.html", context)


def service(request, id):
    service = Services.objects.get(id=id)
    return render(request, "service.html", {"service": service})


def doctor(request, id):
    doctor = Doctors.objects.get(id=id)
    return render(request, 'doctor.html', {'doctor': doctor})


def news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news.html', {'news': news})

def feedback(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        area = request.POST['area']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        feedback = Feedback(fullname=fullname, area=area, email=email, phone_number=phone_number)
        feedback.save()
        return render(request, 'index.html')
    else:
        redirect(index)

def services(request, id):

    services = Services.objects.get(id=id)
    return render(request, 'index.html', {
        'services': services
    })

def advice(request, id):

    advice = Advices.objects.get(id=id)
    return render(request, 'rede.html', {'advice': advice})


def rebot(request):
    doctors = Doctors.objects.all()
    news = News.objects.all()
    service = Services.objects.all()
    about_us = AboutUs.objects.all()
    advice = Advices.objects.all()
    contacts = Contacts.objects.all()
    address = Address.objects.all()
    products = Products.objects.all()
    context = {
        'doctors': doctors,
        'news': news,
        'service': service,
        'about_us': about_us,
        'advice': advice,
        'contacts': contacts,
        'address': address,
        'products': products,

    }
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        area = request.POST['area']
        feedback = Feedback(fullname=fullname, area=area, email=email, phone_number=phone_number)
        feedback.save()
        return render(request, 'index.html', context)
    else:
        return render(request, "index.html", context)