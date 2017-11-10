from django.shortcuts import render
from .forms import TranslationCreateForm

def translation_create(request):

    form = TranslationCreateForm()
    context = {
        'form': form
    }
    return render(request, 'translation/form.html', context)