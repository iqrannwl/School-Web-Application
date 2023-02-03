from django.db import models
from .managers import StudentManager
from django.contrib.auth.models import User

class Project(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='project/')
    date=models.DateTimeField(auto_now=True)
    start_date=models.DateTimeField()
    detail=models.TextField()
    amount_required=models.IntegerField()
    progress=models.CharField(max_length=100)

class Event(models.Model):
    image=models.ImageField(upload_to='event/')
    title=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    detail=models.TextField()
    class Meta:
        ordering=['-date']    





class Testimonial(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='testimonial/')
    desc=models.TextField()
    status= models.BooleanField(
        ('active'),
        default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects=models.Manager()

  






class Regisration(models.Model):
    image=models.ImageField(upload_to='usermedia/')
    username=models.CharField(max_length=100,unique=True)
    Full_name=models.CharField(max_length=100,blank=True,null=True)
    father_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,unique=True,blank=True,null=True)
    phone_no=models.CharField(max_length=11,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    department=models.CharField(max_length=100,blank=True,null=True)
    Passing_Year= models.DateField()

    is_active = models.BooleanField(
        ('active'),
        default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    status=models.BooleanField('public or private',default=False)
    designation=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    reponsibities=models.CharField(max_length=500,blank=True,null=True)

    
   
    
    

    objects=models.Manager()
    public=StudentManager()


    time_stamp=models.DateField(auto_now=True)

    password=models.CharField(max_length=16)


    # def delete(self, using=None, keep_parents=False):
    #     self.image.storage.delete(self.image.name)
    #     super().delete()
        
class Gallery(models.Model):
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='gallery/')



class SchoolInformation(models.Model):
    our_students=models.PositiveBigIntegerField()
    our_teachers=models.PositiveBigIntegerField()
    our_courses=models.PositiveBigIntegerField()
    our_rewards=models.PositiveBigIntegerField()


