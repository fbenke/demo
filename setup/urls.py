from django.conf.urls import url

from .views import add_setup

urlpatterns = [
    url(r'^add/$', add_setup, name='add')
]
