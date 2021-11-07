## from glob import glob
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from pages import setting_dn, setting_sa, setting_sw
from pages import remove, change

# Create your views here.


def index(request):
    return render(request, 'pages/index.html', {})

def image_list(request):
    return render(request, 'pages/list.html', {})


def upload_image(request):

    remove.removefile()

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            imagelist = ImageUpload.objects.all() ##
            context = {'Imagelist' : imagelist} ##
            
            change.change()

            # change.crop()


            # setting_dn.dn()
            # setting_sa.sa()
            # setting_sw.sw()
            
            return render (request, 'pages/crop.html', context) ##list -> crop 211014
    else:
        form = UploadForm()
    return render(request, 'pages/upload.html',{
        'form':form
    })

def crop(request):
    return render(request, 'pages/crop.html', {})


def test(request):
    return render(request, 'pages/hj4.html', {})
    ##211007







