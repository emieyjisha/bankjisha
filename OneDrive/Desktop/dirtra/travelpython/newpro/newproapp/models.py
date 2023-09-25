from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img= models.ImageField(upload_to='pics')
    des= models.TextField()

class Team(models.Model):
    img1=models.ImageField(upload_to='gallery')
    name1=models.CharField(max_length=200)
    desc=models.TextField()

def __str__(self):
    return self.name