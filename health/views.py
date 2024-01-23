from django.shortcuts import render
from django.http import HttpResponse
from.models import *

# Create your views here.
def health(request):
    return render(request,'health.html'),
def appointment(request):
    if request.method == 'POST':
        fullname=request.POST['name']
        email=request.POST['email']
        hospitalName=request.POST['hospital']
        requestingdate=request.POST['requestDate']
        datetime=request.POST['datetime']
        InsertData=appointment(fullname=fullname,Email=email,hosptalName=hospitalName,requestingdate=requestingdate,datetime=datetime)
        InsertData.save()
        return render(request, 'appointment.html')