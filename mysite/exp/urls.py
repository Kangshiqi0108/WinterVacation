from django.urls import path
from exp import views

urlpatterns = [
    path('relr/',views.relrList().as_view()),
    path('relr/<string:pk>/',views.relrDetail().as_view),
]