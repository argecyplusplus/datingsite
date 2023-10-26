from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileViewAll.as_view(), name='allprofiles'), #все профили
    path('<int:pk>/', views.ProfileView.as_view()), #один профиль
    path ('myprofile/', views.MyProfileView, name='myprofile'), #настройка своего профиля
    path ('register/', views.RegisterView.as_view(), name='register'), #регистрация
    path('', views.ProfileViewAllFiltered.as_view(), name='profiles'), #все профили с фильтром
    path('createprofile/', views.CreateMyProfile.as_view(), name='createprofile') #создание профиля
]