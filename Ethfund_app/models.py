from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from sklearn.metrics import max_error
from django.forms import widgets

# Create your models here.

class Category(models.Model):
    titles = models.CharField(max_length=100)
        
    def __str__(self):
        return self.titles


class Projects(models.Model):
    projectname =models.CharField(max_length=100)
    projectdscp = models.CharField(max_length=500,null=True,blank=False)
    projectby = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    goal = models.IntegerField()
    deadline = models.CharField(max_length=10)
    key = models.CharField(max_length=1000)
    image_uploaded = models.ImageField(upload_to='uploaded_images/',null=True,default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    video_uplaoded = models.FileField(upload_to='uploaded_videos/',null=True,blank=True)
    wallet_addr = models.CharField(max_length=100,null=True,blank=True)
    # slug = models.SlugField(max_length = 255)
    
    def __str__(self):
        return self.projectname
    
        
    def get_absolute_url(self):
        return reverse('details', args=[self.slug])

    class Meta:
        verbose_name_plural ="Project List"




