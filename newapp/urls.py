from django.urls import path
from newapp import views


urlpatterns = [
    path('', views.home,name='home'),
    path('arundev/', views.arundev,name='arundev'),
    path('firstassgnmnt/', views.firstassgnmnt,name='firstassgnmnt'),
    path('assgnmnt2/', views.assgnmnt2,name='assgnmnt2')
    ]
 