import imp
from tkinter.tix import Form
from django import forms

class oneInt(forms.Form):
    x=forms.IntegerField(label=' Enter a Number')