from django.urls import path
from newapp import views


urlpatterns = [
    path('', views.home,name='home'),
    path('arundev/', views.arundev,name='arundev'),
    path('firstassgnmnt/', views.firstassgnmnt,name='firstassgnmnt'),
    path('assgnmnt2/', views.assgnmnt2,name='assgnmnt2'),
    path('assgnmnt3/', views.assgnmnt3,name='assgnmnt3'),
    path('bootstrap/', views.bootstrap,name='bootstrap'),
    path('assgnmnt4/', views.assgnmnt4,name='assgnmnt4'),
    path('assgnmnt5/', views.assgnmnt5,name='assgnmnt5'),
    path('assgnmnt6/', views.assgnmnt6,name='assgnmnt6'),
    path('assgnmnt7/', views.assgnmnt7,name='assgnmnt7'),
    path('assgnmnt8/', views.assgnmnt8,name='assgnmnt8'),
    path('assgnmnt9/', views.assgnmnt9,name='assgnmnt9'),
    path('assgnmnt10/', views.assgnmnt10,name='assgnmnt10'),
    ]
 