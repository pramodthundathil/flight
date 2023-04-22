from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name= 'home'), 
    path('login',views.signin,name ='login'),
    path('register',views.register,name ='register'),
    path('index',views.index,name='index'),
    
    path('signout',views.signout,name='signout'),
    path('user_page',views.user_page,name = 'user_page'),
    path('airport_page',views.airport_page,name = 'airport_page')
]