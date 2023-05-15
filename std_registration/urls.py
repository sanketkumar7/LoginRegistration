from django.urls import path
from . import views
urlpatterns = [
    path('registration/<str:username>',views.std_registration_view,name='stdregistration'),
    path('display/',views.display_view,name='display'),
    path('update/<int:pk>',views.update_view,name='update'),
    path('delete/<int:pk>',views.delete_view,name='delete'),
    path('student-list-view/',views.student_list_view.as_view(),name='student_list_view'),
    path('student-detail-view/<int:pk>/',views.student_detail_view.as_view(),name='student_detail_view')
]
