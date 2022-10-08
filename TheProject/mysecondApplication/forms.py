from math import fabs
from socket import fromshare
from tkinter.ttk import Style
from django import forms 

class form2(forms.Form):
    x=forms.CharField( label="Please enter your messsage:  ", required=False, initial="my message", help_text=" enter a messge")