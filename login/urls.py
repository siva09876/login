from django.urls import path
from login import views

urlpatterns=[
    path('',views.home,name='home'),
    path('main',views.main,name='main'),
    path('register',views.register,name='register'),
    path('update/<str:pk>/',views.update_status,name='update'),
    path('complaint',views.complaint,name='complaint')
]