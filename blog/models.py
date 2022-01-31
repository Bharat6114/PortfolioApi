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
class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Blogs(models.Model):
    blog_title = CharField(max_length=250)
    blog_image = models.ImageField(upload_to="blogs", null=True)
    blog_description = TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category, related_name="categoreis")
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.blog_title)
class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return (self.blog)
class Reply(models.Model):
    Comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    replyer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    reply =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
