from unicodedata import category
from django.contrib import admin

# Register your models here.
from blog.models import Category,Blogs
admin.site.register(Category)
admin.site.register(Blogs)