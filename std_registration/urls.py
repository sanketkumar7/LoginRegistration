from django.urls import path
from . import views
urlpatterns = [
    path('registration/<str:username>',views.std_registration_view,name='stdregistration'),
    path('display/',views.display_view,name='display'),
    path('update/<int:pk>',views.update_view,name='update'),
    path('delete/<int:pk>',views.delete_view,name='delete')
]
