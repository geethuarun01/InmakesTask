from django.urls import path
from. import views

app_name= 'credentials'

urlpatterns = [

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('details', views.details, name='details'),

]
