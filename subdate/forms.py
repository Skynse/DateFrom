from django import forms

class DateForm(forms.Form):
    initial = forms.DateField()
    final = forms.DateField()
    result = forms.CharField()