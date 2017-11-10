from django import forms


# 번역을 할 텍스트를 넣는 form
class TranslationCreateForm(forms.Form):
    pre_translated_text = forms.CharField(widget=forms.Textarea)


# 번역 수정을 제안할 텍스트를 넣는 form
class TranslationEditForm(forms.Form):
    edited_translated_text = forms.CharField()
