from urllib import request
import django
from django import forms
from datetime import datetime
class myform(forms.Form):
    levels=(
        (1,'first'),
        (2,'second'),
        (3,'third'),
        (4,'fourth'),
    )
    departments=(
        ('MI','Medical Informatics'),
        ('IT','Information Technology'),
        ('IS','Information System'),
        ('CS','Computer Science'),
        ('AI','Artificial Intelligence'),
    )
    x1=forms.IntegerField(label='Enter num',max_value=10,min_value=5,required=False)
    x2=forms.CharField(label=' Enter text -',required=False)
    x3=forms.BooleanField(label='Are you Happy',required=False)
    x4=forms.ChoiceField(label='choise your level',choices=levels,initial=(3,'third'))
    x5=forms.DateField(label='enter your birthday',initial=datetime.now())
    x6=forms.DateTimeField(label='enter your birthday',initial=datetime.now())
    x7=forms.EmailField(label='Enter Yor Email')
    x8=forms.URLField(label='Enter Url:')
   # x9=forms.DurationField(label='Enter Duration')
    x10=forms.DecimalField(label='Enter Your GPA',max_digits=6)
    x11=forms.TimeField(label='Enter Time')
    x12=forms.MultipleChoiceField(label='choise your Department',choices=departments)