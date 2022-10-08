from django.shortcuts import render

# Create your views here.
from .models import Department

def retrieveDepartments(request):
    x=Department.objects.all()
    return render(request,'BookApp/listalldepartments.html',{'departments':x})


def deptDisplay(request,dept_id):
    dept=Department.objects.get(pk=dept_id)
    return render(request,'BookApp/Department.html',{'Department':dept})