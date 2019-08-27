from django.shortcuts import render,redirect
from .models import *
from .forms import Employee_form
from django.http import *
from django.urls import reverse

def home(request):
        
   if request.method=='POST':
        form=Employee_form(request.POST)
        if form.is_valid():
             form.save()
             return display(request)
             #return HttpResponseRedirect('empreg/display.html')
    
   else:
        form=Employee_form()
   return render(request,'empreg/register.html',{'form':form})
   
def display(request):
     obj=Employee.objects.all()
     return render(request, 'empreg/display.html' ,{'obj':obj})

def search(request):
    form=Searchfrom()
    res=render(request,'empreg/search.html',{'form':form})

def searchnew(request):
    from=Searchfrom(request.POST)	
    b=models.Employee.objects.filter(name=from.data['name'])
    res=render (request,'empreg/search.html',{'from':from,'b':b})
    return res

 