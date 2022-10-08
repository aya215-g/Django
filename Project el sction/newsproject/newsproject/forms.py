from django import forms

class RegEmpForm(forms.Form):
    name = forms.CharField(label="Name: ")
    salary = forms.FloatField(label="Salary: ")
    emp_email = forms.EmailField(label="E-mail: ")
    address = forms.CharField(label="Address: ")
    

