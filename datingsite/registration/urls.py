from django.urls import include, path
from registration.views import index

urlpattern = [
    path('', index, name='index')
]