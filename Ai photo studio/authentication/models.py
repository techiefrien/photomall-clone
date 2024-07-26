from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class userProfile(baseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='profile')
    image = models.ImageField(upload_to='profile_images' , blank = False , null = False)
    shop_name = models.CharField(max_length=300)
    city = models.CharField(max_length=200 ,  blank = False , null = False)
    district = models.CharField(max_length=200 ,  blank = False , null = False)
    address = models.TextField(  blank = False , null = False )
    pin_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=10)
    is_approved = models.BooleanField(default = True)


    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['user']
    
 