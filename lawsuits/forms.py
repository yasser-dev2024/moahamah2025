from django import forms
from .models import Lawsuit

class LawsuitForm(forms.ModelForm):
    class Meta:
        model = Lawsuit
        fields = ['title', 'client_name', 'case_type', 'notes', 'status']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
