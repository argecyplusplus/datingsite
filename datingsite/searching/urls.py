from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormViewAll.as_view()),
    path('<int:pk>/', views.FormView.as_view()),
]