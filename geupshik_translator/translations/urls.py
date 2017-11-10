from django.conf.urls import url

from . import views
from .views import TranslatorList

urlpatterns = [
    url(r'^$', TranslatorList.as_view(), name='create')
]
