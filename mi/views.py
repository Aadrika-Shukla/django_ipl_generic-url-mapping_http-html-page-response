from django.shortcuts import render
from django.http import HttpResponse


#
def hitman(request):
    return HttpResponse('Rohit Sharma is now former captain of Mumbai Indians')

def rohit(request):
    return render(request,'rohit.html')


# Create your views here.
