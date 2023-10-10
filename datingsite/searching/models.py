from django.db import models

# Create your models here.
class Form(models.Model):
    genders = (
        ('М', 'Парень'),
        ('Ж', 'Девушка')
    )
    searching_for_list = (
        ('М', 'Парня'),
        ('Ж', 'Девушку'),
        ('В', 'Кого угодно')
    )

    name = models.CharField ('Имя', max_length=50)
    avatar = models.ImageField ('Фото', default='https://www.meme-arsenal.com/memes/9deabcb50a53c324b3a4981528215040.jpg')
    age = models.IntegerField("Возраст")
    gender = models.CharField ("Пол", choices=genders, max_length=1, default=genders[0])
    searching_for = models.CharField ("Ищу", choices=searching_for_list, max_length=1, default=searching_for_list[1])
    description = models.TextField ('О себе', max_length=50)
    #... можно расширить

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"

    def __str__(self):
        return f'{self.name}'