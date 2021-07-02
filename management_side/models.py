from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.

class member(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    photo=models.ImageField(blank=True,upload_to='usersImages/%Y/%m/%d/', null=True,default="person.png")
    GENDER=(('Female','Female'),('Male','Male'))
    gender= models.CharField(max_length=50,null=True,choices=GENDER)
    username= models.CharField(max_length=50,null=True)
    first_name= models.CharField(max_length=50,null=True)
    last_name= models.CharField(max_length=50,null=True)
    email= models.CharField( max_length=50,null=True)
    country = models.CharField(max_length=60,default="",null=True)
    city = models.CharField(max_length=60,default="",null=True)
    state = models.CharField(max_length=60,default="",null=True)
    street = models.CharField(max_length=60,default="",null=True)
    building_num = models.CharField(max_length=60,default="",null=True)
    dept_num = models.CharField(max_length=60,default="",null=True)    
    join_date= models.DateTimeField(auto_now=False, auto_now_add=True)
    phones = JSONField(default=list)

    class Meta:
        abstract = True


class Customer(member):
    def __str__(self):
        return self.username

    # @classmethod
    # def create(cls,user,username,first_name,gender,last_name,country,state,city,street,building_num,dept_num,phones):
    #     customer =cls(user=user,username=username,first_name=first_name,last_name=last_name
    #                             ,gender=gender,country=country,state=state,city=city,street=street,building_num=building_num,
    #                             dept_num=dept_num,phones=phones)
    #     return customer


class Floor(models.Model):
    FLOOR =(
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),        
        ('5th','5th'),
        ('6th','6th')
    )
    floor_id=models.CharField(max_length=30,choices=FLOOR,primary_key=True)

    def __str__(self):
        return self.floor_id


class Manager(member):
    working_floor =models.ForeignKey(Floor,on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.username


class Category(models.Model):
    floor_id =models.ForeignKey(Floor,on_delete=models.CASCADE)
    cat_id = models.AutoField(primary_key=True)
    cat_name =models.CharField(max_length=10,default="")

    def __str__(self):
        return str(self.cat_id) 


class Shelf(models.Model):
    cat_id =models.ForeignKey(Category,on_delete=models.CASCADE)
    shelf_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.shelf_id)


class BookPosition(models.Model):
    floor_id =models.ForeignKey(Floor,on_delete=models.CASCADE)
    shelf_id =models.ForeignKey(Shelf,on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("floor_id", "shelf_id","cat_id"),)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    isbn =models.IntegerField()
    book_seat =models.ForeignKey(BookPosition,on_delete=models.CASCADE,default="")
    title =models.CharField(max_length=40,default="")
    language =models.CharField(max_length=30,default="")
    bookPhoto = models.ImageField(upload_to ='bookPhoto/%Y/%m/%d/',default="")
    description =models.TextField(max_length=400,default="")
    demurage =models.IntegerField(default=0)
    author_name =models.CharField(default="",max_length=30)
    version_number =models.CharField(max_length=10,default="")
    year =models.DateField(max_length=10,default="")

    CONDITION =(
        ('bad','bad'),
        ('normal','normal'),
        ('good','good'),
    )
    condition =models.CharField(max_length=40,choices=CONDITION,default="")
    
    STATUS =(
        ('pending','pending'),
        ('delivered','delivered'),
        ('out of date','out of date'),
        ('available','available')
    )
    
    status =models.CharField(max_length=30,choices=STATUS,default="")
    def __str__(self):
        return str(self.book_id)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)     
  
    def amount(self):
        book_amount =Book.objects.get(isbn=self.isbn).count()
        return book_amount
       

class Issue(models.Model):
    issue_id=models.AutoField(primary_key=True,default=4)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default="")
    manager = models.ForeignKey(Manager,null=True, on_delete=models.SET_NULL)
    issue_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    issue_for = models.DateField(max_length=10,default="")
    last_edit= models.DateField(auto_now=True, auto_now_add=False,null=True)

    def __str__(self):
       return str(self.issue_id)


# class Condition(models.Model):
#     CONDITION 🙁
#         ('bad','bad'),
#         ('normal','normal'),
#         ('good','good'),
#     )
#     condition =models.CharField(max_length=40,choices=CONDITION,primary_key=True)


# class Status(models.Model):
#     STATUS 🙁
#         ('pending','pending'),
#         ('delivered','delivered'),
#         ('out of date','out of date'),
#     )
#     status =models.CharField(max_length=30,choices=STATUS,primary_key=True)

#  condition =models.ForeignKey(Condition,on_delete=SET_NULL)
#     status =models.ForeignKey(Status, on_delete=SET_NULL)