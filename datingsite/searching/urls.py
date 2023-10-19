from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormView.as_view()),
]