from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manja(request):
    
    return render(request,'manjappada.html')
