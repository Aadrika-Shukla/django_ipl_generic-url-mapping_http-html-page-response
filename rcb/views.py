from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kohli(request):
    return HttpResponse('Virat Kohli is captain of Royal Challengers Bangalore')

def virat(request):
    return render(request,'virat.html')