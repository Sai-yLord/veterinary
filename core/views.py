from django.core.paginator import Paginator
from django.shortcuts import render


from django.views import View, generic

from core.models import *

def doctor_page(request, id):
    doctor = Doctors.objects.get(id=id)
    return render(request, 'rede.html', {'doctor': doctor})


def news_page(request, id):
    news = News.objects.get(id=id)
    return render(
        request,
        "topic2.html",
        {"news":  news}
    )


# def service_page(request, id):
#     services = Services.objects.get(id=id)
#     return render(request, 'index.html', {
#         'services': services
#     })

def advice_page(request, id):
    advice = Advices.objects.get(id=id)
    return render(request, 'rede.html', {'advice': advice})


class Index(generic.ListView):
    def get(self, request):
        news = News.objects.all()
        service = Services.objects.all()
        about_us = AboutUs.objects.all()
        doctors = Doctors.objects.all()
        advice = Advices.objects.all()
        contacts = Contacts.objects.all()
        address = Address.objects.all()
        contact_list = Products.objects.all()
        paginator = Paginator(contact_list, 1)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'news': news,
            'service': service,
            'about_us': about_us,
            'advice': advice,
            'contacts': contacts,
            'address': address,
            'page_obj': page_obj,
            'doctors': doctors,

        }
        return render(request, "index.html", context)

    def post(self, request):
        if request.method == "GET":
            return render(request, "index.html")
        if request.method == 'POST':
            fullname = request.POST['fullname']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            area = request.POST['area']
            feedback = Feedback(fullname=fullname, area=area, email=email, phone_number=phone_number)
            feedback.save()
            return render(request, 'index.html')
        else:
            return render(request, "index.html")


