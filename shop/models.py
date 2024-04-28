from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
 
class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name
 
class Product(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  original_price=models.FloatField(null=False,blank=False)
  selling_price=models.FloatField(null=False,blank=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name
 
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)

  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price

class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)  

class Order(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  name =  models.CharField(max_length=150,null=False)
  lname =  models.CharField(max_length=150,null=False)
  email = models.CharField(max_length=150,null=False)
  phone = models.CharField(max_length=150,null=False)
  address = models.TextField(null=False)
  city = models.CharField(max_length=150,null=False)
  state = models.CharField(max_length=150,null=False)
  country = models.CharField(max_length=150,null=False)
  pincode = models.CharField(max_length=150,null=False)
  total_cost = models.FloatField(null=False)
  payment_mode = models.CharField(max_length=150,null=False)
  payment_id = models.CharField(max_length=150,null=True)
  orderstatus=(
    ('pending','pending'),
    ('out for shipping','out for shipping'),
    ('completed','completed'),
  )
  status = models.CharField(max_length=150,choices=orderstatus,default='pending')
  message = models.TextField(null=True)
  tracking_no = models.CharField(max_length=150,null=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return '{}-{}'.format(self.id,self.tracking_no)

class OrderItem(models.Model):
  order=models.ForeignKey(Order,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  price = models.FloatField(null=False)
  quantity=models.IntegerField(null=False)

  def __str__(self) :
    return '{}-{}' .format(self.order.id,self.tracking_no)

class Profile(models.Model):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
  phone = models.CharField(max_length=150,null=False)
  address = models.TextField(null=False)
  city = models.CharField(max_length=150,null=False)
  state = models.CharField(max_length=150,null=False)
  country = models.CharField(max_length=150,null=False)
  pincode = models.CharField(max_length=150,null=False)
  created_at=models.DateTimeField(auto_now_add=True)  
  
  def __str__(self) :
    return self.user.username
