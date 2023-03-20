from django.http import HttpResponse
from django.shortcuts import render
from .models import Service
# Create your views here.
def index(request):
    service=Service.objects.all()
    return render(request,'index.html',{'service':service})