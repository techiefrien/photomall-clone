from django.db import models
from django.contrib.auth.models import User
from .utils import getEventKey


# Create your models here.


class Events(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="events")
    name = models.CharField(max_length=500)
    key = models.CharField(max_length=10 , unique=True , null=True , blank=True , default=None)
    image = models.ImageField(upload_to='events_logo')
    upload_range = models.PositiveBigIntegerField(default=5)
    is_upload = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


    def save(self  , *args , **kwargs):
        if self.key == None:
            self.key = getEventKey()
        super(Events , self).save(*args , **kwargs)
    

    def __str__(self):
        return str(self.name) + " " + self.key 
    

class pictures(models.Model):
    event = models.ForeignKey(Events , on_delete=models.CASCADE , related_name='photos')
    photo = models.ImageField(upload_to='Events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return str(self.event)
    


class eventAttender(models.Model):
    event = models.ForeignKey(Events , on_delete=models.CASCADE , related_name='attenders')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    selfie = models.ImageField(upload_to='selfies')

    def __str__(self):
        return  str(self.event ) + str(self.name) + str(self.phone)



class selfie_matches(models.Model):
    attender = models.ForeignKey(eventAttender , on_delete=models.CASCADE , related_name='photos')
    photo = models.ForeignKey(pictures , on_delete=models.CASCADE)


    def __str__(self):
        return str(self.attender) + str(self.photo)



class notification(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="nofications")
    Heading = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return str(self.user) + " " + str(self.Heading)