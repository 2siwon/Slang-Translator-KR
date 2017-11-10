from django.shortcuts import render

from translation.models import Visitor
from .forms import TranslationForm


def translation_create(request):
    """
    1. 일반어 form을 GET요청인 경우 보여주며,
    2. form을 POST 요청으로 제출한 경우 Translation 모델을 저장한다.

    이 때, 저장을 하는 순간
    2-1) 번역을 요청한 방문자를 author 필드를 추가하고,
    2-2) pre_translated_text로 들어온 텍스트를 번역한 후 post_translated_text에 저장한다.
    """
    # 읿반어를 번역하기 버튼, POST 요청으로 form을 제출한 경우
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            translation = form.save(commit=False)
            # 임시로 첫번째 방문자를 번역요청한 방문자로 지정
            translation.author = Visitor.objects.get(pk=1)
            # 번역 모델이 저장이 models.py의 오버라이드된
            # save를 호출하면서, post_translated_text 필드를 채워서 저장함
            translation.save()
    # POST 요청이 아닌 경우; 처음 번역 form을 보여주는 경우
    else:
        form = TranslationForm()
        # 번역된 translation 모델이 저장이 안된 상태
        translation = None
    context = {
        'form': form,
        'translation': translation
    }
    return render(request, 'translation/form.html', context)
