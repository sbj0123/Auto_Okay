from django import forms
from .models import Recording

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = 'audioFile',

