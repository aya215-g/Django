from django.shortcuts import render

# Create your views here.
from .forms import myform
def start(request):
    m='test'
    m1='test'
    m3='test'
    m4='test'
    m5='test'
    m6='test'
    m7='test'
    m8='test'
    m9='test'
    m10='test'
    m11='test'
    m12='test'
    form=myform()
    if request.method=='POST':
        form=myform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            m=cd['x']
            m1=cd['y']
            m2=cd['z']
            if m2==True:
                m3='since you  are happy give me 100$'
            else:
                m3='we are sorry'
            m4=cd['w']
            m5=cd['x5']
            m6=cd['x6']
            m7=cd['x7']
            m8=cd['x8']
            m10=cd['x10']
            m11=cd['x11']
            m12=cd['x12']


    return render(request,'mypage.html',{'form':form,'output':m,'output2':m1,'output3':m3,'output4':m4,'output5':m5,'output6':m6,'output7':m7,
    'output8':m8,
    'output10':m10,
    'output11':m11,
    'output12':m12})