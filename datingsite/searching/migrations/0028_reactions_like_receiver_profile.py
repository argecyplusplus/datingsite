# Generated by Django 4.2.6 on 2023-11-03 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0027_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='like_receiver_profile',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='like_receiver_profile', to='searching.profile', verbose_name='Анкета отправителя'),
        ),
    ]
