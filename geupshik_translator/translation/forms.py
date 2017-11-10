from django import forms

from .models import Translation


# Translation 모델에 대한 form
class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = [
            'pre_translated_text',
            'edited_translated_text',
        ]
