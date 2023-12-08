from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User name")
    file = forms.FileField(label='Profile Picture')
    email = forms.EmailField(label= 'User email')
    age = forms.IntegerField(label="Age")
    weight = forms.FloatField(label='Weight')
    balance = forms.DecimalField(label='User Balance')
    check = forms.BooleanField(label='Single')
    birthday = forms.DateField(label="Birthday")
    appointment = forms.DateTimeField(label='Date Time for appointment')
    CHOICE = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    siez = forms.ChoiceField(choices=CHOICE)
    MEAL = [('P', 'Pepperoni'), ('B', 'Beef'), ('M', 'Mashroom')]
    pizza = forms.MultipleChoiceField(choices=MEAL)