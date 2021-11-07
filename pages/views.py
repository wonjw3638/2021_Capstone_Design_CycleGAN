## from glob import glob
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from pages import setting_dn, setting_sa, setting_sw
from pages import setting_nd, setting_as, setting_ws
from pages import remove, removepng, change, resize, copypaste, copyoutput, bitchange

# Create your views here.


#211021
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse

def main_view(request):
    remove.removefile()
    removepng.removefile()

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'message':'works'})
    context = {'form':form}

    return render(request, 'pages/main.html', context)

def select(request):

    resize.resize()
    remove.removefile()
    change.change()
    bitchange.bitchange()
    copypaste.copy()

    return render(request, 'pages/upload_hj.html', {})

def index(request):
    remove.removefile()
    removepng.removefile()
    return render(request, 'pages/index_hj.html', {})

def day(request):
    setting_dn.dn()
    copyoutput.copy()
    return render(request, 'pages/day.html', {})

def night(request):
    setting_nd.nd()
    copyoutput.copy()
    return render(request, 'pages/night.html', {})

def spring(request):
    setting_sa.sa()
    copyoutput.copy()
    return render(request, 'pages/spring.html', {})

def summer(request):
    setting_sw.sw()
    copyoutput.copy()
    return render(request, 'pages/summer.html', {})

def autumn(request):
    setting_as.asp()
    copyoutput.copy()
    return render(request, 'pages/autumn.html', {})

def winter(request):
    setting_ws.ws()
    copyoutput.copy()
    return render(request, 'pages/winter.html', {})

