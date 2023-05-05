from django import forms
from .models import admin
from django.core.validators import EmailValidator

class loginForm(forms.ModelForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),label='Username :')
    password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password :')
    def clean(self):
        cleaned_data=super().clean()
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        print('--',username,'--',password)
        if not admin.objects.filter(username=username,password=password).exists():
            self.add_error('username','Invalid Username or Password')
        return cleaned_data
    class Meta:
        model=admin
        fields=('username','password')
class SignupForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','pattern':'[a-zA-Z0-9]{5,12}'}),required=True)
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),validators=[EmailValidator],required=True)
    master_key1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    master_key2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    confirm_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    def clean(self):
        cleaned_data=super().clean()
        username=self.cleaned_data['username']
        master_key1=self.cleaned_data['master_key1']
        master_key2=self.cleaned_data['master_key2']
        if admin.objects.filter(username=username).exists():
                raise forms.ValidationError('Username already Exists.')
        if master_key1!='12345':
            self.add_error('master_key1','Wrong master_key1, contact your manager')
        if master_key2!='12345':
            self.add_error('master_key2','Wrong master_key2, contact your manager')
        if self.cleaned_data['password']!=self.cleaned_data['confirm_password']:
            self.add_error('password','password didn\'t matched')
        return cleaned_data
        