from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(userProfile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'shop_name' , 'city' , 'district' , 'address' , 'pin_code' , 'phone_number' , 'created_at' , 'updated_at']

