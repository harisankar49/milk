from django.shortcuts import render
from django.http import HttpResponse
from .models import service
# Create your views here.
def index(request):
    obj=service.objects.all()

    return render(request,'index.html',{'result':obj})
