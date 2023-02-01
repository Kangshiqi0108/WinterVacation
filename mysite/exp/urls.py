from django.urls import path

from . import views

urlpatterns = [
    path('', views.LangList.as_view(), name='LangList'),
    path('<str:pk>/', views.LangDetail.as_view(), name='LangDetail'),
    
]
