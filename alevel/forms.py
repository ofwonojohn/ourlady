from django import forms
from .models import ALevelMark, ALevelSubject
from core.models import Term

class ALevelMarkForm(forms.ModelForm):
    class Meta:
        model = ALevelMark
        fields = ['subject', 'term', 'score']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'term': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }

    def clean_score(self):
        score = self.cleaned_data['score']
        if not 0 <= score <= 100:
            raise forms.ValidationError("Score must be between 0 and 100.")
        return score
