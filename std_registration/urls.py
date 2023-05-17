from django.urls import path
from . import views
urlpatterns = [
    path('registration/<str:username>',views.std_registration_view,name='stdregistration'),
    path('display/',views.display_view,name='display'),
    path('update/<int:pk>',views.update_view,name='update'),
    path('delete/<int:pk>',views.delete_view,name='delete'),
    path('student-list-view/',views.student_list_view.as_view(),name='student_list_view'),
    path('student-detail-view/<int:pk>/',views.student_detail_view.as_view(),name='student_detail_view'),
    path('contact-us',views.contact_us_view,name='contact_us')
]

from apscheduler.schedulers.background import BackgroundScheduler
from .views import myfunction
scheduler = BackgroundScheduler(jobstore='sqlalchemy')
def scheduled_function():
    myfunction()
scheduler.add_job(scheduled_function, 'cron', hour=17,minute=52,replace_existing=True)
print('Yes')
scheduler.start()

