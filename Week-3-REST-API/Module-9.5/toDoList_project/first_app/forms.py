from django import forms
from first_app.models import TaskMode

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskMode
        fields = ['taskTitle', 'taskDescription']