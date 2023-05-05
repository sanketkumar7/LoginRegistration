from django.contrib import admin
from .models import admin as A
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','password']
admin.site.register(A,LoginAdmin)