from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileViewAll.as_view(), name='allprofiles'),
    path('<int:pk>/', views.ProfileView.as_view()),
    path ('myprofile/', views.MyProfileView, name='myprofile'),
    path ('register/', views.RegisterView.as_view(), name='register'),
    path('', views.ProfileViewAllProtected, name='profiles'),
    path('createprofile/', views.CreateMyProfile.as_view(), name='createprofile')
]