from django.db import models

# Create your models here.
class Student(models.Model):
    full_name=models.CharField(max_length=200,default="")
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    address=models.TextField()
    state=models.CharField(max_length=100)
    image=models.ImageField(null=True,upload_to='std_registration/images/',default='')