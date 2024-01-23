from django.shortcuts import render
from django.http import HttpResponse
from.models import *

# Create your views here.
def appointment(request):
    if request.method == 'POST':
        fullname=request.POST['name']
        email=request.POST['email']
        hospitalname=request.POST['hospital']
        requestingdate=request.POST['requestDate']
        datetime=request.POST['datetime']
        InsertData= appointment(fullname=fullname,email=email,hosptalname=hospitalname,requestingdate=requestingdate,datetime=datetime)
        InsertData.save()
        
    return render(request, 'appointment.html')
        
def health(request):
             return render(request,'health.html')