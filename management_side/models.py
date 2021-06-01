from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class member(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    image=models.ImageField(blank=True, null=True,default="person.png")
    GENDER=(('Female','Female'),('Male','Male'))
    username= models.CharField(max_length=50,null=True)
    first_name= models.CharField(max_length=50,null=True)
    last_name= models.CharField(max_length=50,null=True)
    gender= models.CharField(max_length=50,null=True,choices=GENDER)
    email= models.CharField( max_length=50,null=True)
    city= models.CharField( max_length=50,null=True)
    country= models.CharField( max_length=50,null=True)
    address= models.CharField( max_length=50,null=True)    
    date_created= models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        abstract = True



class Customer(member):
    def __str__(self):
        return self.username



# class Customer(models.Model):
#     user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
#     image=models.ImageField(blank=True, null=True,default="person.png")
#     GENDER=(('Female','Female'),('Male','Male'))
#     username= models.CharField(max_length=50,null=True)
#     first_name= models.CharField(max_length=50,null=True)
#     last_name= models.CharField(max_length=50,null=True)
#     gender= models.CharField(max_length=50,null=True,choices=GENDER)
#     email= models.CharField( max_length=50,null=True)
#     city= models.CharField( max_length=50,null=True)
#     country= models.CharField( max_length=50,null=True)
#     address= models.CharField( max_length=50,null=True)    
#     date_created= models.DateTimeField(auto_now=False, auto_now_add=True)
#     def __str__(self):
#         return self.username



class Manager(member):
    working_floor= models.CharField( max_length=50,null=True)
    def __str__(self):
        return self.username



class Tag(models.Model):
    name= models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
   
class Book(models.Model):
    STATUS =(
        ('available','available'),
        ('non-available','non-available'),
    )
    name= models.CharField(max_length=50,null=True)
    author= models.CharField(max_length=50,null=True)
    category= models.CharField(max_length=50,null=True)
    shelf= models.CharField(max_length=50,null=True)
    status= models.CharField(max_length=50,null=True,choices=STATUS)
    condition= models.CharField(max_length=50,null=True)
    date_created= models.DateTimeField(auto_now_add=True)
  #  tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
  
class Issue(models.Model):
    STATUS =(
        ('pending','pending'),
        ('delivered','delivered'),
        ('out of date','out of date'),
    )
  #  customer=models.ForeignKey(Customer,null=True,on_delete =models.SET_NULL) 
    book=models.ForeignKey(Book,null=True,on_delete =models.SET_NULL)
    tag=models.ManyToManyField(Tag)
    status =models.CharField(max_length=50,null=True,choices=STATUS)
    date_created= models.DateTimeField(auto_now_add=True)

