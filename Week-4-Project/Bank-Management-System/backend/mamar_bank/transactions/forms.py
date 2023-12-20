from django import forms
from . models import Transaction

class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]
    
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__()
        self.fields['transaction_type'].disabled = True # first this field will be disable
        self.fields['transaction_type'].widget = forms.HiddenInput() # and this field will be hide from user
        
    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    
    
    
class DepositForm(TransactionsForm):
    def clean_amount(self): # way to filter amount field in model form
        min_deposit = 100
        amount = self.cleaned_data.get('amount') # get data from frontend
        if amount < min_deposit:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit} $'
            )
        return amount
    

class WithdrawForm(TransactionsForm):
    def clean_amount(self):
        account = self.account
        max_withdraw_amount = 20000
        min_withdraw_amount = 500
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )
        
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at time at most {max_withdraw_amount} $'
            )
        
        if amount < balance:
            raise forms.ValidationError(
                f'Salar fokir aga bank a taka deposite kor tor account a matro {balance} $ acha'
            )
            
        return amount
    

class LoanRequestForm(TransactionsForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount