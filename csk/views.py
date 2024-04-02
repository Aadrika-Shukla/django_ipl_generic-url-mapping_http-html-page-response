from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def dhoni(request):
    return HttpResponse('Mahendra Singh Dhoni is now former CHENNAI SUPER KINGS CAPTAIN')

def msd(request):
    return render(request,'msd.html')