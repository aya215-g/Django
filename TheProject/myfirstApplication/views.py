from django.shortcuts import render

def firstfunc(request):
    return render(request,'myfirstApplication/firstpage.html',{'message':'Hello from First Application'})

