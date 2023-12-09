from typing import Any
from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="User name", initial='MD Al Amin', help_text='Total length must be 70 char', required=False, disabled=False, widget= forms.TextInput(attrs= {'id' : 'text-are', 'class' : 'class1 class2, class3', 'placeholder' : 'Enter Your Name'}))
    # file = forms.FileField(label='Profile Picture')
    # email = forms.EmailField(label= 'User email')
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField(label='Weight')
    # balance = forms.DecimalField(label='User Balance')
    # check = forms.BooleanField(label='Single')
    # birthday = forms.DateField(label="Birthday")
    # appointment = forms.DateTimeField(label='Date Time for appointment')
    # CHOICE = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # siez = forms.ChoiceField(choices=CHOICE)
    # MEAL = [('P', 'Pepperoni'), ('B', 'Beef'), ('M', 'Mashroom')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)

    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='Age')
    weight = forms.FloatField(label='Weight', required= False)
    birthday = forms.DateField(label='Birthdaey', widget= forms.DateInput(attrs={'type' : 'date'}))
    appoinment = forms.DateTimeField(label='Appoinment', widget= forms.DateInput(attrs={'type' : 'datetime-local'}))

    CHOICE = [('S', 'Small'), ('M', "Medium"), ('L', "Large")]
    size = forms.ChoiceField(choices=CHOICE, widget= forms.RadioSelect)

    MEAL = [('B', 'Beef'), ('M', "Maton"), ("NaN", 'Nothing')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget= forms.CheckboxSelectMultiple)

 

 # new Form and its a form validitations
# class StudentData(forms.Form):
#     name = forms.CharField(label="Full Name", widget= forms.TextInput(attrs={'placeholder' : 'Enater Your Full Name'}))
#     email = forms.EmailField(label='Email', widget= forms.EmailInput(attrs={'placeholder' : 'Enater Your Email'}))
    
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName) <= 10:
    #         raise forms.ValidationError("Enter Name it will be atleat 10 Charecter")
    #     else:
    #         return valName
        

    # def clean_email(self):
    #     valEmail = self.cleaned_data['email']
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Email must be contain .com not Others")
    #     else:
    #         return valEmail


    # def clean(self):
    #     cleaned_data = super().clean()
    #     valName = self.cleaned_data['name']
    #     valEmail = self.cleaned_data['email']

    #     if len(valName) <= 10:
    #         raise forms.ValidationError("Enter Name it will be atleat 10 Charecter")
        
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Email must be contain .com not Others")

# build in validators functions

def len_check(value):
    if len(value) <= 10:
        raise forms.ValidationError('Enter a vlue at least 10 charecter')

class StudentData(forms.Form):
    name = forms.CharField(label="Full Name", validators=[validators.MinLengthValidator(10, message='Enter a name atleat 10 charecter')])
    email = forms.EmailField(label='Email', validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(label='Age', validators=[validators.MaxValueValidator(34, message="Age maximum 32"), validators.MinValueValidator(24, message='Age at leat 24')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='File extentation ended with .pdf')])

    text = forms.CharField(validators=[len_check])


class PasswordValidtionPorject(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[len_check])
    password = forms.CharField(widget=forms.PasswordInput)
    confo_pass = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        # valName = self.cleaned_data['name']
        valPass = self.cleaned_data['password']
        valConfo_pass = self.cleaned_data['confo_pass']

        if valConfo_pass != valPass:
            raise forms.ValidationError('Password doesnot match')
        


    



