
from turtle import title
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# from kishan.views import scheme


# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=122)
   email = models.CharField(max_length=122)
   subject = models.CharField(max_length=122)
   message = models.TextField()
   date = models.DateField()
def __str__(self):
    return self.name

class Register(models.Model):
   fname = models.CharField(max_length=122)
   lname = models.CharField(max_length=122)
   email = models.CharField(max_length=122)
   number = models.CharField(max_length=12)
   address = models.CharField(max_length=122)
   # password = models.PasswordField()
   # address=models.CharField(widget=models.address)
   date = models.DateField()
   
   def __str__(self):
      return self.fname
   
   
   
class Schemes(models.Model):
   scheme_icon=models.CharField(max_length=50)
   scheme_title=models.CharField(max_length=50)
   # schemes_desc=models.HTMLField()
   scheme_desc=models.TextField()
   
   # def __str__(self):
   #    return self.scheme_icon
# class SchemesAdmin(admin.ModelAdmin):
#     list_display=('scheme_icon','scheme_title','scheme_desc')
# admin.site.register(Schemes,SchemesAdmin)