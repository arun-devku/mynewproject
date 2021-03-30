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
    path('assgnmnt11/', views.assgnmnt11,name='assgnmnt11'),
    path('assgnmnt12/', views.assgnmnt12,name='assgnmnt12'),
    path('assgnmnt13/', views.assgnmnt13,name='assgnmnt13'), 
    path('assgnmnt14/', views.assgnmnt14,name='assgnmnt14'),
    path('assgnmnt15/', views.assgnmnt15,name='assgnmnt15'),
    path('mypro/', views.mypro,name='mypro'),  
    path('mypro2/', views.mypro2,name='mypro2'),
    path('fbbase/', views.fbbase,name='fbbase'), 
    path('fblog1/', views.fblog1,name='fblog1'), 
    path('fblog2/', views.fblog2,name='fblog2'),
    path('fblog3/', views.fblog3,name='fblog3'),
    path('mypro1/', views.mypro1,name='mypro1'),
    path('new1/', views.new1,name='new1'),
    
    ]
 