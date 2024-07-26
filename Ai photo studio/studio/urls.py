from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name='home') , 
    path('events/' , views.events , name='events') , 
    path('upload-photos/<str:event_key>' , views.uploadPhotos , name='upload-photos') , 
    path('gallery/<str:key>' , views.gallery , name='gallery') , 
    path('selfie-gallery/<str:key>' , views.selfie_gallery , name='selfie-gallery') , 
    path('event-qr-genrator/<str:key>' , views.event_qr_generator , name='event-qr-generator') , 
    path('upload-selfie/<str:key>' , views.uploadSelfie , name='upload-selfie') , 
    path('create-profile/<str:id>' , views.create_profile , name='create-profile') , 
    path('attender-matches/<str:id>' , views.attender_matches , name='attender-matches')
]