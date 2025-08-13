from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=20)
    viewPassword=models.CharField(max_length=200,null=True)

class Customer(models.Model):
    customer= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20)
    Image=models.ImageField(upload_to="Image",null=True)
    Address=models.CharField(max_length=200)
    status=models.CharField(max_length=20,default='pending')

class Service_center(models.Model):
    servicecenter= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Servicecentername1=models.CharField(max_length=20)
    Email1=models.EmailField()
    Phonenumber1=models.IntegerField(null=True)
    Password1=models.CharField(max_length=20)
    Address1=models.CharField(max_length=200)
    status=models.CharField(max_length=20,default='pending')

class Solar_products(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Productname=models.CharField(max_length=20)
    Image1=models.ImageField(upload_to="Image",null=True)
    Price=models.IntegerField()
    Stock=models.CharField(max_length=200,null=True)
    Description=models.CharField(max_length=200)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    order=models.ForeignKey('Order',on_delete=models.CASCADE,null=True)
    solarproducts = models.ForeignKey(Solar_products, on_delete=models.CASCADE,null=True)
    qty=models.IntegerField(null=True)
    amt=models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=40,default='pending')

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField(null=True)
    solarproducts = models.ForeignKey(Solar_products, on_delete=models.CASCADE,null=True)
    Date=models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=40,default='pending')

class Booking(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True) 
    Productname1=models.CharField(max_length=20,null=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    Message2=models.CharField(max_length=200,null=True)
    servicecenter= models.ForeignKey(Service_center,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')
    Price1=models.IntegerField(null=True)
    solarproducts = models.ForeignKey(Solar_products, on_delete=models.CASCADE,null=True)

class Payment(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    servicecenter=models.ForeignKey(Service_center,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')

class Feedback(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Message=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=20,default='pending')
    reply=models.CharField(max_length=200,null=True)

class Request(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Message2=models.CharField(max_length=200,null=True)
    Unit=models.IntegerField(null=True)
    Price2=models.IntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=20,default='pending')