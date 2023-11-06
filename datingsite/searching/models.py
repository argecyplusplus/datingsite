from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    genders = (
        ('Парень', 'Парень'),
        ('Девушка', 'Девушка')
    )
    point_of_searching_list = (
        ('Отношения', 'Отношения'),
        ('Свидания', 'Свидания'),
        ('Дружба', 'Дружба'),
        ('Общение', 'Общение'),
    )

    name = models.CharField ('Имя', max_length=50)
    avatar = models.ImageField ('Фото', upload_to='photos/users', default='photos/default_avatar.jpg')
    age = models.IntegerField("Возраст")
    gender = models.CharField ("Пол", choices=genders, max_length=30, default=genders[0])
    point_of_searching = models.CharField ("Цель знакомства", choices=point_of_searching_list, max_length=30, default=point_of_searching_list[0])
    city = models.CharField ('Город', max_length=100, default="Не указано")
    description = models.TextField ('О себе', max_length=50)
    social = models.CharField ('Ссылка на соцсеть', max_length=50, default='@name')
    user = models.OneToOneField(User, verbose_name='Автор анкеты', on_delete=models.CASCADE)
    
    #для фильтрации поиска по возрасту
    age_search_min = models.IntegerField("Возраст поиска (от)", default=16)
    age_search_max = models.IntegerField("Возраст поиска (до)", default=100)

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"

    def __str__(self):
        return f'{self.name}, {self.age}, {self.city}'

class Reactions(models.Model):
    like_sender = models.ForeignKey(User, verbose_name='Отправитель', related_name='like_sender', on_delete=models.CASCADE)
    like_receiver = models.ForeignKey(User, verbose_name='Получатель', related_name='like_receiver', on_delete=models.CASCADE)
    like_sender_profile = models.ForeignKey(Profile, verbose_name='Анкета отправителя', related_name='like_sender_profile', default=5,on_delete=models.CASCADE)
    like_receiver_profile = models.ForeignKey(Profile, verbose_name='Анкета отправителя', related_name='like_receiver_profile', default=5,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Реакция"
        verbose_name_plural = "Реакции"

    def __str__(self):
        return f'{self.like_sender}, {self.like_receiver}'