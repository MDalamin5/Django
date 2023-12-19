from django.contrib.auth.forms import UserCreationForm
from . consnts import GENDER_TYPE, ACCOUNT_TYPE
from django import forms
from django.contrib.auth.models import User
from . models import UserBankAccount, UserAddress

class UserRegistrationsForm(UserCreationForm):
    birth_date = forms.DateField(widget= forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField(choices = GENDER_TYPE)
    account_type = forms.ChoiceField(choices = ACCOUNT_TYPE)
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500 '
                )
            })
            
            
# user can be update: name, email            
class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget= forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField(choices = GENDER_TYPE)
    account_type = forms.ChoiceField(choices = ACCOUNT_TYPE)
    street_address = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500 '
                )
            })
        
        # if user has an account
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserBankAccount.DoesNotExist:
                user_account = None
                user_address = None
                
            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['gender'].initial = user_account.gender
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country
                
    def save(self, commit = True):
        user = super().save(commit=False)
        if commit:
            user.save()
            
            
            user_account, created = UserBankAccount.objects.get_or_create(user=user) #if user is exists the account will be updated and not have account then created a new accaount and its contains in crated....
            user_address, created = UserAddress.objects.get_or_create(user=user)
            
            user_account.account_type = self.cleaned_data['account_type']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()
            
            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()
            
        return user


