from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exclude = ['address']
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll',
            'address' : 'Student Address',
            'father_name' : 'Father Name'
        }
        widgets = {
            'name' : forms.TextInput(),
            
        }
        help_texts = {
            'name' : 'Enter Your Full Name',
            'roll' : 'Enter Your Roll',
            'address' : 'Write your Address',

        }
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }