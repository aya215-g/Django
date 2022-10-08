from distutils.command.upload import upload
from pyexpat import model
from tkinter import image_names
from django.db import models

# Create your models here.
class ImageCollectionModel(models.Model):
    image_name= models.CharField(max_length=200)
    image_description =models.TextField()
    image_time = models.DateTimeField(auto_now_add=True)
    img_file=models.ImageField(upload_to='upload_images/')

   
    def __str__(self):
        return self.image_name


    