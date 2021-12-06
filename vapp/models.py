from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)
    Age = models.IntegerField()
    City = models.CharField(max_length=50)
    Images = models.ImageField(upload_to="pics/" , null=True, blank=True, )
    

    def __str__ (self):
        return self.Username 


class Userdata(models.Model):
    Username = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)
    Age = models.DateField()
    City = models.CharField(max_length=50)
    Images = models.ImageField(upload_to="pics/" , null=True, blank=True, )
    Phone = models.CharField(max_length=50)
    
    

    def __str__ (self):
        return self.Username 


class task(models.Model):
    Username = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)
    Age = models.DateField()
    City = models.CharField(max_length=50)
    Pwd = models.CharField(max_length=50)
    RPwd = models.CharField(max_length=50)
    Images = models.ImageField(upload_to="pics/" , null=True, blank=True )
    Phone = models.CharField(max_length=10)
    
    

    def __str__ (self):
        return self.Username 

class adminpage (models.Model):
    Username = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)
    Age = models.DateField()
    City = models.CharField(max_length=50)
    Pwd = models.CharField(max_length=50)
    RPwd = models.CharField(max_length=50)
    Images = models.ImageField(upload_to="picss/" , null=True, blank=True, )
    Phone = models.CharField(max_length=50)
    
    

    def __str__ (self):
        return self.Username 




