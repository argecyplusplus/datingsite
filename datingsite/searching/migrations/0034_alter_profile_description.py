# Generated by Django 4.2.6 on 2023-11-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0033_newpair_viewed1_newpair_viewed2_reactions_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(max_length=300, verbose_name='О себе'),
        ),
    ]