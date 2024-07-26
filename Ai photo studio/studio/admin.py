from django.contrib import admin
from .models import *
# Register your models here.


class pictureAdmin(admin.StackedInline):
    model = pictures
    

@admin.register(Events)
class eventAdmin(admin.ModelAdmin):
    inlines = [pictureAdmin,]
    list_display = ['name' , 'key' , 'upload_range' , 'is_upload' , 'created_at' , 'updated_at']
    fields = ['user' , 'name' , 'image' , 'upload_range' , 'is_upload']



class selfieAdmin(admin.ModelAdmin):
    list_display = ['name' , 'event' , 'phone' , 'selfie']
admin.site.register(eventAttender , selfieAdmin)