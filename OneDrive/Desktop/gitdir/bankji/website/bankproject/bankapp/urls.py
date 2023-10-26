from.import views
from django.urls import path


urlpatterns = [

     path('',views.demo,name='demo'),

     path('register/', views.register, name='register'),
     path('loginn/', views.loginn, name='loginn'),
     path('logout/', views.logout, name='logout'),
     path('new/',views.new,name='new'),
     path('form/',views.form,name='form'),
     path('getdata/',views.getdata,name="getdata"),
     path('msgpas/',views.message,name='message'),

]
