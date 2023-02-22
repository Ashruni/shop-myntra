from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class regshopmodels(models.Model):
    shopname = models.CharField(max_length=30)
    shoploc = models.CharField(max_length=30)
    shopid = models.IntegerField()
    email = models.EmailField()
    mobnum = models.IntegerField()
    password = models.CharField(max_length=30)
    confirmpass = models.CharField(max_length=30)
    # id is there automaically gen
    # __str__:The str method returns a human readable or informal string representatio
    # n of an object
    def __str__(self):
        return self.shopname + " ,id - " + str(self.shopid)

# class userloginmodels(models.Model):
#     userid= models.IntegerField

class shopuploadmodels(models.Model):
    # userid=models.IntegerField()
    shopid=models.IntegerField()
    # shopname = models.CharField(max_length=30)
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productdescription = models.CharField(max_length=150)
    productfile = models.ImageField(upload_to ='Myntraapp/static')
    def __str__(self):
        return self.productname + " , id- " + str(self.shopid)

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.username
class cart(models.Model):
    uc = models.IntegerField()
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productdescription = models.CharField(max_length=150)
    productfile = models.ImageField()
    def __str__(self):
        return self.productname
class wishlist(models.Model):
    # userid = models.IntegerField()
    uid=models.IntegerField()
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productdescription = models.CharField(max_length=150)
    productfile = models.ImageField()
    def __str__(self):
        return self.productname

class buy(models.Model):
    productname = models.CharField(max_length=30)
    productprice = models.IntegerField()
    productdescription = models.CharField(max_length=150)
    productfile = models.ImageField()
    quantity= models.IntegerField()
    def __str__(self):
        return self.productname

class customercard(models.Model):
    cardname= models.CharField(max_length=30)
    cardnumber= models.CharField(max_length=30)
    cardexpiry= models.CharField(max_length=30)
    securitycode=models.CharField(max_length=30)
    def __str__(self):
        return self.cardname


class shopnotification(models.Model):
    content = models.CharField(max_length=200)
    shopnottime = models.DateTimeField(auto_now_add=True)


class usernotification(models.Model):
    content = models.CharField(max_length=200)
    usernottime = models.DateTimeField(auto_now_add=True)

# class customerlocationmodel(models.Model):
#     name= models.CharField(max_length=10)
#     number = models.IntegerField()
#     address= models.CharField(max_length=30)
#     pincode = models.IntegerField()
#     locality= models.CharField(max_length=30)
#     city = models.CharField(max_length=10)
#     state = models.CharField(max_length=10)


