from django import forms
from django.forms import Textarea

from .models import Translation

# Translation 모델에 대한 form
class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = [
            'pre_translated_text',
            'edited_translated_text',
        ]
        widgets = {
            'pre_translated_text': Textarea(
                attrs={
                    'class': 'translate-form',
                    'placeholder': '번역할 텍스트를 입력하세욧',
                }
            ),
        }
