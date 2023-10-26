# Generated by Django 4.2.6 on 2023-10-26 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searching', '0014_profile_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='АвторАнкеты'),
        ),
        migrations.DeleteModel(
            name='MyProfile',
        ),
    ]
