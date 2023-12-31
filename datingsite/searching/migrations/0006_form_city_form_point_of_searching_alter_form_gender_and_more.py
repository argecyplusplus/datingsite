# Generated by Django 4.2.6 on 2023-10-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0005_form_searching_for_alter_form_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='city',
            field=models.CharField(default='Не указано', max_length=100, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='form',
            name='point_of_searching',
            field=models.CharField(choices=[('О', 'Отношения'), ('С', 'Свидания'), ('Д', 'Дружба'), ('Т', 'Общение')], default=('О', 'Отношения'), max_length=1, verbose_name='Цель знакомства'),
        ),
        migrations.AlterField(
            model_name='form',
            name='gender',
            field=models.CharField(choices=[('М', 'Парень'), ('Ж', 'Девушка')], default=('М', 'Парень'), max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='form',
            name='searching_for',
            field=models.CharField(choices=[('М', 'Парня'), ('Ж', 'Девушку'), ('В', 'Кого угодно')], default=('Ж', 'Девушку'), max_length=1, verbose_name='Ищу'),
        ),
    ]
