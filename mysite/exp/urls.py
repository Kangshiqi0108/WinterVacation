from django.urls import path
from exp import views

urlpatterns = [
    path('relr/',views.relrList().as_view()),
    path('relr/<str:pk>/',views.relrDetail().as_view()),
    path('stul/',views.studentList().as_view()),
    
]