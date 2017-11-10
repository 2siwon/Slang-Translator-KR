from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.translation_create, name='home')
]
