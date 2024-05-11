from django import forms
from .models import TasksModel

class TasksForm(forms.ModelForm):
    class Meta():
        model = TasksModel
        fields = ['status']