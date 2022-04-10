from django import forms


class ContactoForm(forms.Form):
    name = forms.CharField()
    lasname = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    messege = forms.CharField()

