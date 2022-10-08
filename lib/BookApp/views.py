from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path
from requests import post

from BookApp.forms import DepartmentForm

# Create your views here.
from .models import Department

def retrieveDepartments(request):
    x=Department.objects.all()
    return render(request,'BookApp/listalldepartments.html',{'departments':x})


def deptDisplay(request,dept_id):
    dept=Department.objects.get(pk=dept_id)
    return render(request,'BookApp/Department.html',{'Department':dept})


from .forms import BookForm, DepartmentForm
from django.shortcuts import redirect
def AddNewDepartment(request):
    form=DepartmentForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_departments')

    return render(request, 'BookApp/newdpartment.html',{'form':form })

def addNewBook(request,dept_id):
    dept=Department.objects.get(pk=dept_id)

    form=BookForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        form=form.save(commit=False)
        form.dept=dept
        form.save()
        return redirect('display_department', dept_id=dept_id)


    return render(request,'BookApp/addnewBook.html',{'Department':dept,'form':form})
