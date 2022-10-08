from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import PrimeForm
from .PrimeTest import isPrime
from .forms import WorldcupForm
import random


def hello_world(request):
    return HttpResponse('hello')

@csrf_exempt
def addxy(request):
    if(request.method == 'POST'):
        x = int(request.POST.get('firstvalue'))
        y = int(request.POST.get('secondvalue'))
        z = x+y
        return HttpResponse('Result = ' +str(z))
    else:
        return HttpResponse('''
         <form action="addtwonumbers" method="POST">
        <p>
           <label for="firstvalue">Enter First Number</label>
           <input type="text" name="firstvalue"/>
        </p>

        <p>
            <label for="secondvalue">Enter Second Number</label>
            <input type="text" name="secondvalue"/>
        </p>

        <button type="submit" > ADD </button>

    </form>
        ''')



from .forms import InputForm

def add(request):
    z = 0
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            z = x + y

    return render(request, 'pages/addition.html', {'form': form, 'output':z})



def performArithmetic(request):
    x = 1
    y = 1
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            y = cd['y']
            

    return render(request, 'pages/arithmetic.html', {'form': form, 
    'x': x, 
    'y': y,
    'r1': x+y,
    'r2': x-y,
    'r3': x*y,
    'r4': x//y,
    'r5': x%y})





def prime(request):
    b = False
    form = PrimeForm()
    if request.method == 'POST':
        form = PrimeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
            b = isPrime(x)

    if b == False:
        m = "This Number Is Not Prime"   
    else:
        m = "This Number Is Prime" 

    return render(request, 'pages2/prime.html', {'form': form, 'output':m})








def worldcup(request):
    m = ''
    form = WorldcupForm()
    if request.method == 'POST':
        form = WorldcupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['countries']
            y = x.split('-')
            for i in range(int(len(y)/2)):
                z = random.sample(y, k=2)
                for i in z:
                    y.remove(i)
                    m += z[0] + 'X' + z[1] + '\n'
   

    return render(request, 'pages2/worldcup.html', {'form': form, 'output':m})

