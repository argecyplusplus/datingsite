from django.db import models

# Create your models here.
class Form(models.Model):
    genders = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
        ('Г', 'Гей'),
        ('Л', 'Лесбиянка'), 
        ('С', 'Сковородкасексуал')
    )

    name = models.CharField ('Имя', max_length=50)
    age = models.IntegerField("Возраст")
    gender = models.CharField ("Пол", choices=genders, max_length=1) #если true то мужчина

    description = models.TextField ('О себе', max_length=50)
    #... можно расширить

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"

    def __str__(self):
        return f'{self.name}'