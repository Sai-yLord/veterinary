from django.http import HttpResponseRedirect
from django.shortcuts import render

from core.models import Service, Doctors, News, AboutUs, Advice, Contacts, Address, Feedback


def index(request):
    doctors = Doctors.objects.all()
    news = News.objects.all()
    service = Service.objects.all()
    about_us = AboutUs.objects.all()
    advice = Advice.objects.all()
    contacts = Contacts.objects.all()
    address = Address.objects.all()
    context = {
        'doctors': doctors,
        'news': news,
        'service': service,
        'about_us': about_us,
        'advice': advice,
        'contacts': contacts,
        'address': address,

    }
    if request.method == 'POST':
        fullname = request.POST['fullname']
        area = request.POST['area']
        phone_number = request.POST['phone_number']
        feedback = Feedback(fullname=fullname, area=area, phone_number=phone_number)
        feedback.save()
        return render(request, 'index.html', context)
    else:
        return render(request, "index.html", context)


def service(request, id):
    service = Service.objects.get(id=id)
    return render(request, "service.html", {"service": service})


def doctor(request, id):
    doctor = Doctors.objects.get(id=id)
    return render(request, 'doctor.html', {'doctor': doctor})


def new(request, id):
    new = News.objects.get(id=id)
    return render(request, 'news.html', {'new': new})


