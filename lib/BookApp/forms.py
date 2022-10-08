
from django  import forms
from .models import Department , Book


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=['dept']