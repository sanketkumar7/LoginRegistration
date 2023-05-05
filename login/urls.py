from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome_view,name='welcome'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_key_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('aboutus/',views.about_us_view,name="aboutus")
]
