from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField("E-mail", max_length=50)
    password = models.CharField("Пароль", max_length=50)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.name}'