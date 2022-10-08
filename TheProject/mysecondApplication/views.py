from django.shortcuts import render

# Create your views here.
from mysecondApplication.forms import form2

# Create your views here.

def second(request):
   

    return render(request, 'secondapp/secondpage.html', {'message': "Hi This My Second App"})