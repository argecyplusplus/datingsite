from django.db import models

# Create your models here.
class Form(models.Model):
    genders = (
        ('Парень', 'Парень'),
        ('Девушка', 'Девушка')
    )
    searching_for_list = (
        ('Парня', 'Парня'),
        ('Девушку', 'Девушку'),
        ('Кого угодно', 'Кого угодно')
    )
    point_of_searching_list = (
        ('Отношения', 'Отношения'),
        ('Свидания', 'Свидания'),
        ('Дружба', 'Дружба'),
        ('Общение', 'Общение'),
    )

    name = models.CharField ('Имя', max_length=50)
    avatar = models.ImageField ('Фото', upload_to='photos/users', default='default_avatar.jpg')
    age = models.IntegerField("Возраст")
    gender = models.CharField ("Пол", choices=genders, max_length=30, default=genders[0])
    searching_for = models.CharField ("Ищу", choices=searching_for_list, max_length=30, default=searching_for_list[1])
    point_of_searching = models.CharField ("Цель знакомства", choices=point_of_searching_list, max_length=30, default=point_of_searching_list[0])
    city = models.CharField ('Город', max_length=100, default="Не указано")
    description = models.TextField ('О себе', max_length=50)
    #... можно расширить

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"

    def __str__(self):
        return f'{self.name}'