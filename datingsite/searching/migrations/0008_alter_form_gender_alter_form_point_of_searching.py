# Generated by Django 4.2.6 on 2023-10-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0007_alter_form_gender_alter_form_point_of_searching_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='gender',
            field=models.CharField(choices=[('Парень', 'Парень'), ('Девушка', 'Девушка')], default=('Парень', 'Парень'), max_length=30, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='form',
            name='point_of_searching',
            field=models.CharField(choices=[('Отношения', 'Отношения'), ('Свидания', 'Свидания'), ('Дружба', 'Дружба'), ('Общение', 'Общение')], default=('Отношения', 'Отношения'), max_length=30, verbose_name='Цель знакомства'),
        ),
    ]
