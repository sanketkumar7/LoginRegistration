from django.db import models
from django.core.validators import FileExtensionValidator,MaxValueValidator,MinValueValidator
from .validators import MaxFileSizeValidator,MinFileSizeValidator
# Create your models here.
class Student(models.Model):
    full_name=models.CharField(max_length=200,default="")
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    address=models.TextField()
    state=models.CharField(max_length=100)
    image=models.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png']),MaxFileSizeValidator(1000*1024,message='File size should not exceed 1mb.'),MinFileSizeValidator(1024*10,message='File size should be at least 10kb')],null=True,upload_to='std_registration/images/',default='')