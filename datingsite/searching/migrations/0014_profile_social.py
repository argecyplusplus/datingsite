# Generated by Django 4.2.6 on 2023-10-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0013_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social',
            field=models.TextField(default='@name', max_length=50, verbose_name='СсылкаНаСоцсеть'),
        ),
    ]
