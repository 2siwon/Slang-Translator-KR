from django.shortcuts import render


def translator_home(request):
    context = {

    }
    return render(request, 'translation/home.html', context)