from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'case_type', 'description', 'attachment']
        labels = {
            'title': 'عنوان القضية',
            'case_type': 'نوع القضية',
            'description': 'وصف القضية',
            'attachment': 'مرفقات (اختياري)',
        }
