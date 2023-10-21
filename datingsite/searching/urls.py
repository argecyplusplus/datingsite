from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileViewAll.as_view()),
    path('<int:pk>/', views.ProfileView.as_view()),
    path ('myprofile/', views.MyProfileView, name='myprofile'),
    path ('register/', views.RegisterView.as_view(), name='register'),
]