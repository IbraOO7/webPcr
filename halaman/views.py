from django.shortcuts import render, redirect
from . models import *

def error_404_view(request, exception):
    return render(request, '404.html')

def index(request):
    data1 = Gallery.objects.all()
    data2 = Tentang.objects.all()
    data3 = Harga.objects.all()
    data4 = FAQ.objects.all()
    data5 = Kontak.objects.all()
    data6 = Pelayanan.objects.all().order_by('id')[:1]
    data7 = Metode.objects.all()
    data8 = Sponsor.objects.all()
    
    context = {
        "data1": data1, "data2": data2, "data3": data3, 
        "data4": data4, "data5": data5, "data6": data6, "data7": data7, "data8": data8
    } 
    return render(request, 'laman.html', context)

def register(request):
    return render(request, 'register.html')


