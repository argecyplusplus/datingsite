# Generated by Django 4.2.7 on 2023-11-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0037_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social',
            field=models.CharField(default='@nam e', max_length=50, verbose_name='Ссылка на соцсеть'),
        ),
    ]
