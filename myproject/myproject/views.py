from ast import If
import imp
import string
from django.http import HttpResponse
from django.urls import is_valid_path
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django import forms
import random
from .forms import oneInt  
from .forms import  oneInt




def Testview(request):
    m=' '
    sum=0
    forms=[]
    for i in range(1,12):
        form=oneInt(prefix='form'+str(i),initial={'x':i})
        forms.append(form)
    if request.method=='POST':
        for i in range(1,12):
            form=oneInt(request.POST,prefix='form'+str(i))
            if form.is_valid():
                cd=form.cleaned_data
                x=cd['x']
                m+=str(x)+"+"
                sum+=x
        m=m[:-1]+' = '+str(sum)
    return render(request,'page/Test.html',{'forms':forms,'output':m})
    
