from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.indeksik, name='index'),
    url(r'czylizetak', views.aha, name='ixdex')
]
