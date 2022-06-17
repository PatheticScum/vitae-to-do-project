from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from todo.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = [
            'title',
            'content'

        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control mb-4',
                }
            ),

        }
