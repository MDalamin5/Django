from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User name")
    email = forms.EmailField(label= 'User email')