from django.db import models

# Create your models here.
class Shop(models.Model):
    name=models.CharField(max_length=40)
    type=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.FileField(upload_to='images',default='null.jpg')

class Category(models.Model):
    type=models.CharField(max_length=20)


class Customer(models.Model):
    cname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=50,default='pass')
    number=models.IntegerField()

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=500)

class Cart(models.Model):
    price=models.IntegerField()
    product_id=models.ForeignKey(Shop, on_delete = models.CASCADE, null = True, blank=True)
    user_id=models.ForeignKey(Customer, on_delete = models.CASCADE, null = True, blank=True)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    quantity=models.IntegerField()
    total=models.IntegerField(default=0)
class Checkout(models.Model):
    fname=models.CharField(max_length=40,default='null')
    lname=models.CharField(max_length=50,default='null')
    email=models.EmailField(max_length=50,default='null')
    country=models.CharField(max_length=20,default='null')
    address=models.CharField(max_length=50,default='null')
    city=models.CharField(max_length=20,default='null')
    phone=models.IntegerField(default=0)
    postcode=models.IntegerField(default=0)
