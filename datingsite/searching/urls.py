from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProfileView.as_view(), name='oneprofile'), #один профиль
    path ('myprofile/', views.MyProfileView, name='myprofile'), #настройка своего профиля
    path ('register/', views.RegisterView.as_view(), name='register'), #регистрация
    path('', views.ProfileViewAllFiltered.as_view(), name='profiles'), #все профили с фильтром
    path('createprofile/', views.CreateMyProfile.as_view(), name='createprofile'), #создание профиля
    path ('reactions/', views.ReactionsView.as_view(), name='reactions'), #реакции на мою анкету
    path ('reactions/<int:pk>/', views.ReactionProfile.as_view(), name='reaction_profile'), #вывод анкеты, которая отправила лайк
    path ('start', views.startworking, name='start'), # кнопка под добро пожаловать
    path ('reactions/like/<int:pk>/', views.ReactView.as_view(), name='like'), #отправить лайк
    path ('reactions/like_reply/<int:pk>/', views.ReactReplyView.as_view(), name='like_reply'), #отправить взаимку
    path ('reactions/dislike_reply/<int:pk>/', views.ReactReplyViewDislike.as_view(), name='dislike_reply'), #отправить отказ
]