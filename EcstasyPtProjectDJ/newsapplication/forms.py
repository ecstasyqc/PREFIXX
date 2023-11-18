from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AcriclesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anonse', 'absolute_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of alert'
            }),
            "anonse": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anonse of alert'
            }),
            "absolute_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of alert'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of alert publishing'
            }),
        }