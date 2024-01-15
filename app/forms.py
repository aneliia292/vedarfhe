from django import forms
from .models import *


class TodoForm(forms.Form):
    task = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'task',
                                                                         'placeholder': 'Task'}))
    data = forms.DateField(widget=forms.DateInput())
    status = forms.BooleanField()


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={'class': 'task', 'placeholder': 'Task'}),
            'date': forms.DateInput(),
            'status': forms.CheckboxInput(attrs={'class': 'checkbox'})
        }


class TodoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['task', 'status']
