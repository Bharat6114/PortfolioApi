from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField,DateField,EmailField
from django.db.models.fields.files import ImageField
from django.conf import settings
from django.utils.timezone import datetime

# Create your models here.
class Aboutme(models.Model):
    name = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    dob = models.DateField(null=False)
    phone_no = models.CharField(max_length=10)
    pic = models.ImageField(upload_to = "portfolio",null=True)
    aboutme =models.TextField(max_length=1000)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)
    fb_address = models.CharField(max_length=50,default=' ')
    insta_address = models.CharField(max_length=50,default=' ')
    linkdin_id = models.CharField(max_length=50,default= ' ')
    github_id = models.CharField(max_length=50,default=' ')
    twitter_id = models.CharField(max_length=50,default=' ')
    def __str__(self):
        return self.name
class Myskils(models.Model):
    title = models.CharField(max_length=200)
    description =models.CharField(max_length=300)
    skill_measure = models.IntegerField(null=False)
    pic = models.ImageField(upload_to = "portfolio",null=True)

    def __str__(self):
        return self.title

class Workingstyle(models.Model):
    working_style = models.CharField(max_length=150)
    def __str__(self):
        return (self.working_style)

class Myexperience(models.Model):
    startdate = models.DateField()
    enddate = models.DateField(default='Present') 
    post = models.CharField(max_length=100)
    name_of_company = models.CharField(max_length=100)
    address_of_company = models.CharField(max_length=100)
    years = models.IntegerField(default=0)
    
    def __str__(self):
        return (self.name_of_company)

class Offering(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to = "portfolio",null=True)
    def __str__(self):
        return (self.title)

class Myprojects(models.Model):
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50)
    language_used =models.CharField(max_length=20)
    project_description = models.TextField(max_length=500)
    project_image = models.ImageField(upload_to = "portfolio",null=True)

    def __str__(self):
        return (self.project_name)

class Uploadcv(models.Model):
    title=models.CharField(max_length=50)
    cv=models.FileField(upload_to="portfolio")

