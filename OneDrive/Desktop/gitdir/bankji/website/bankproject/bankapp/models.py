from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class district(models.Model):
    districtname = models.CharField(max_length=100,blank=True,null=True)


class Branch(models.Model):
    distid = models.ForeignKey(district, on_delete=CASCADE,blank=True,null=True)
    branchname = models.CharField(max_length=100)



