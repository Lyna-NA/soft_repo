from django.db import models

# Create your models here.


class Member(models.Model):
    username= models.CharField(max_length=50,null=True)
    first_name= models.CharField(max_length=50,null=True)
    last_name= models.CharField(max_length=50,null=True)
    gender= models.CharField(max_length=50,null=True)
    email= models.CharField( max_length=50,null=True)
    city= models.CharField( max_length=50,null=True)
    country= models.CharField( max_length=50,null=True)
    address= models.CharField( max_length=50,null=True)    
    date_created= models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name

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
  
class Order(models.Model):
    STATUS =(
        ('pending','pending'),
        ('delivered','delivered'),
        ('out of date','out of date'),
    )
    member=models.ForeignKey(Member,null=True,on_delete =models.SET_NULL) #بنفعش ال اوردر يروح  ل كذ كاستمر ولا بنفع الاوردر نفسه يكون لكذا كتاب =one to many
    book=models.ForeignKey(Book,null=True,on_delete =models.SET_NULL)
    tag=models.ManyToManyField(Tag)
    status =models.CharField(max_length=50,null=True,choices=STATUS)
    date_created= models.DateTimeField(auto_now_add=True)


# ال فورن كي بيكون ضكن ال اي دي للجدول تبع  الاوردر يعني بنفعش يتكرروا لنفس الاوردر
# يعني الاوردر الواحد بيكون لكتاب واحد  و بخص كاستمر واحد  بس 
# يعني الاوردر بيروحش لكذا حدا و لا بيكون لكذا كتاب 
# بس الكاستمر بيروح لكذا اوردر و الكتاب كمان ممكن ينطلب من كذا حدا
# يعني one to many 
#من جهة الكاستر و من جهة ال بوكس

