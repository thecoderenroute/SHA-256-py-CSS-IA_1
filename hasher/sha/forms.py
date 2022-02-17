from django import forms

class textForm(forms.Form):
    text = forms.CharField(label='Any text', max_length=100)