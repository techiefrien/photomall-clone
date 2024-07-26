from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from PIL import Image
from io import BytesIO
from . import utils
from .utils import compareFaces
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request , 'index.html')
    return redirect('sign-in')


def events(req):
    events_obj = Events.objects.filter(user = req.user)
    photosCount = pictures.objects.all().count()
    context = {
        'events' : events_obj ,  
        'photoCount': photosCount , 
    }
    return render(req , 'studio/events.html' , context)



def uploadPhotos(request , event_key):

    if request.method == 'POST':
        images = request.FILES.getlist('img')
        event_key = request.POST.get('event_key')
        eventobj = Events.objects.get(key = event_key)
       
        if not eventobj.is_upload:
            return HttpResponse('Your upload permission is blocked . please contact your Support Team')
        
        for img in images:
            if eventobj.upload_range>0:
                img = utils.compressImage(img)
                pictures.objects.create(event = eventobj , photo = img )
                eventobj.upload_range = eventobj.upload_range - 1
                eventobj.save()
                print(eventobj.upload_range)
            else:
                return HttpResponse('Sorry your upload limit is over , please upgrade your plan')
    
        return HttpResponse('reqeust recied !')
    
    return render(request , 'studio/upload_photos.html' , {'event_key':event_key})
    


def gallery(request , key):
    event = Events.objects.get(key = key)
    return render(request , 'studio/gallery.html' , {'event':event})


def selfie_gallery(request , key):
    eventobj = Events.objects.get(key = key)
    return render(request , 'studio/selfies.html' , {"event":eventobj})


def event_qr_generator(request , key):
    event = Events.objects.get(key = key)
    return render(request , 'studio/event_qr.html' , {'event':event})


def uploadSelfie(request , key):
    if request.method == 'POST':
        selfie = request.FILES.get('selfie')
        ekey = request.POST.get('key')
        print(key , selfie)
        eventobj = Events.objects.get(key = ekey)
        eventAttobj = eventAttender.objects.create(
                                event = eventobj , 
                                selfie = selfie
        )
        id = eventAttobj.id
        return redirect(f'/create-profile/{id}')
    eventobj = Events.objects.get(key = key)
    return render(request , 'selfie/upload_selfie.html' , {'event':eventobj})


def create_profile(request , id):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        id = request.POST.get('id')
        print(name , phone , id)
        attobj = eventAttender.objects.get(id = id)
        attobj.name = name
        attobj.phone = phone
        attobj.save()
        return redirect(f'/attender-matches/{attobj.id}')
    print('id :' , id)
    attender = eventAttender.objects.get(id = id)
    return render(request , 'selfie/profile.html' , {'user':attender})

def attender_matches(request , id):
    attender = eventAttender.objects.get(id=id)
    print(id , attender)
    target_img = attender.selfie.path
    print('target image')
    print(target_img)
    matched_pics=[]
    print('input_images')
    for img in attender.event.photos.all():
         input_img = img.photo.path
         is_mateched = compareFaces(target_img, input_img)
         if is_mateched:
             matched_pics.append(img)

    
    return render(request , 'selfie/match_page.html' , {'user':attender , 'matches':matched_pics})


