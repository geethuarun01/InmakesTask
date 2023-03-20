from django.urls import path
from. import views

app_name= 'Bankapp'

urlpatterns = [

    path('',views.index, name='index'),

]
