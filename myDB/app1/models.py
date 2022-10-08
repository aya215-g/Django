from django.db import models

# Create your models here.

class personName(models.Model):

    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName+ " " + self.LastName

        
