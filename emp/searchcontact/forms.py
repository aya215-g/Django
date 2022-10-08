from tkinter.font import names
from django import forms

class searchform(forms.Form):
    name =forms.CharField(label='Enter name :')