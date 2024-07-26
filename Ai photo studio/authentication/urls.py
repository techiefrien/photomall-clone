from django.urls import path 
from . import views 

urlpatterns = [
    path('sign-in/' , views.signIn , name='sign-in') ,
    path('sign-out/' , views.signOut , name='sign-out') ,  
    path('profile-page/' ,  views.profilePage , name='profile-page') , 
    path('settings/' , views.settings , name='settings') , 
    path('edit-profile/' , views.editProfile , name='edit-profile') , 
    path('security/' , views.security , name='security')
]