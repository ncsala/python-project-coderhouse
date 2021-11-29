from django import forms



class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)
    
# class DepartmentForm(forms.Form):
#     name = forms.CharField(max_length=50, unique=True)
#     short_name = forms.CharField(max_length=20, blank=True)
#     anulate = forms.BooleanField(default=False)
    