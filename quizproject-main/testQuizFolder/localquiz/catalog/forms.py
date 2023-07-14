from django import forms

class CatalogStringForm(forms.Form):
    return_string = forms.CharField(label='Return String', max_length=100)
