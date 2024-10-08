from django.db import models

# Create your models here.

class contactdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=300,null=True,blank=True)

class registerdb(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password2=models.CharField(max_length=50,null=True,blank=True)

class cartdb(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    Productname=models.CharField(max_length=50,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)

class checkoutdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Address=models.CharField(max_length=300,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)

