from django.db import models

# Create your models here.
class toreview_mailus(models.Model):
    yourname=models.CharField(max_length=50)
    youremail=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

#class tablebooking(models.Model):
   # gname=models.CharField(max_length=50)
    #gmail=models.EmailField()
    #gphone=models.FloatField()
    #gdate=models.DateField()
    #gtime=models.TimeField()
    #gpeople=models.IntegerField()
    #gmessage=models.TextField()

class guest(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()    
