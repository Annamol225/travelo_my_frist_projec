from django.shortcuts import render
from django.http import HttpResponse
from .models import place, desc


# Create your views her


def fun(request):
    obj=place.objects.all()
    obj1=desc.objects.all()
    return render(request,'index.html',{"results":obj,"result":obj1})

def add(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    num3=num1+num2
    return render(request,'result.html',{"add":num3})


