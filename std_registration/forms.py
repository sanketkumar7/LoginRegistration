from django import forms
from django.core.validators import FileExtensionValidator,RegexValidator
from .models import Student
import datetime

choose_gender=[('Male','Male'),('Female','Female'),('Other','Other')]
union_territories = [
                            ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
                            ("Chandigarh", "Chandigarh"),
                            ("Dadra and Nagar Haveli and Daman and Diu", "Dadra and Nagar Haveli and Daman and Diu"),
                            ("Lakshadweep", "Lakshadweep"),
                            ('Delhi','Delhi')]
STATE_CHOICES = sorted([
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttarakhand', 'Uttarakhand'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('West Bengal', 'West Bengal'),
    ]+union_territories,key=lambda x:x[0])
    
class Student_Registration(forms.ModelForm):
    full_name=forms.CharField(validators=[RegexValidator(regex='[a-zA-Z]{2,30}$',message='only alphabets allowed.')],widget=forms.TextInput(attrs={"class":"form-control"}),max_length=100,required=True)
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=choose_gender,required=True)
    dob=forms.DateField(initial=datetime.date.today,required=True,widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),label='Date of Birth')
    address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class': 'form-control'}),required=True)
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),required=True)
    image=forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'],message='Only .jpg,.jpeg,.png files are allowed.'),])
    def clean(self):
        cleaned_data=super().clean()
        full_name=self.cleaned_data['full_name']
        address=self.cleaned_data['address']
        dob=self.cleaned_data['dob']
        image=self.cleaned_data['image']
        image_size=image.size
        if image_size>1000*1024 or image_size<10*1024:
            self.add_error('image','The image size must be more than 10kb and less than 1mb')

        if Student.objects.filter(full_name=full_name,address=address,dob=dob).exists():
            self.add_error('full_name','Same User Data Request...Full_Name, Date of Birth and Address can\'t be same')

        return cleaned_data
    class Meta:
        model=Student
        fields="__all__"
class Student_Update_Form(forms.ModelForm):
    full_name=forms.CharField(validators=[RegexValidator(regex='[a-zA-Z]{2,30}$',message='only alphabets allowed only.')],widget=forms.TextInput(attrs={"class":"form-control"}),max_length=100,required=True)
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=choose_gender,required=True)
    dob=forms.DateField(initial=datetime.date.today,required=True,widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),label='Date of Birth')
    address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class': 'form-control'}),required=True)
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),required=True)
    image=forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'],message='Only .jpg,.jpeg,.png files are allowed.'),])
    def clean(self):
        cleaned_data=super().clean()
        image=self.cleaned_data['image']
        image_size=image.size
        if image_size>1000*1024 or image_size<10*1024:
            self.add_error('image','The image size must be more than 10kb and less than 1mb')
        return cleaned_data
    class Meta:
        model = Student
        fields = '__all__'
    '''def __init__(self, *args, **kwargs):
        mymodel_instance = kwargs.pop('mymodel_instance', None)
        super(Student_Update_Form, self).__init__(*args, **kwargs)
        if mymodel_instance:
            self.fields['full_name'].initial = mymodel_instance.full_name
            self.fields['gender'].initial = mymodel_instance.gender
            self.fields['dob'].initial = mymodel_instance.dob
            self.fields['address'].initial = mymodel_instance.address
            self.fields['state'].initial = mymodel_instance.state
            self.fields['image'].initial = mymodel_instance.image'''
            