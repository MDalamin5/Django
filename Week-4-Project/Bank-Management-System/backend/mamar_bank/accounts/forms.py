from django.contrib.auth.forms import UserCreationForm
from . consnts import GENDER_TYPE
from django import forms
from django.contrib.auth.models import User
from . models import UserBankAccount, UserAddress

class UserRegistrationsForm(UserCreationForm):
    brith_date = forms.DateField(widget= forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.CharField(max_length=10, choices = GENDER_TYPE)
    street_address = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date', 'gender', 'street_address', 'postal_code', 'city', 'country']
        
    def save(self, commit=True):
        our_user = super().save(commit=False)
        
        if commit == True:
            our_user.save() # save data in user model
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            
            UserBankAccount.objects.create(
                user = our_user,
                account_type = account_type,
                account_no = 100000 + our_user.id,
                birth_date = birth_date,
                gender = gender 
            )
            
            
            UserAddress.objects.create(
                user = our_user,
                street_address = street_address,
                city = city,
                postal_code = postal_code,
                country = country
            )
        return our_user