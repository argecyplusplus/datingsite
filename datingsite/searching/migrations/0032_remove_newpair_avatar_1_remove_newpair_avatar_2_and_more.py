# Generated by Django 4.2.6 on 2023-11-06 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searching', '0031_alter_reactions_like_receiver_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpair',
            name='avatar_1',
        ),
        migrations.RemoveField(
            model_name='newpair',
            name='avatar_2',
        ),
        migrations.RemoveField(
            model_name='newpair',
            name='name_1',
        ),
        migrations.RemoveField(
            model_name='newpair',
            name='name_2',
        ),
        migrations.RemoveField(
            model_name='newpair',
            name='social_1',
        ),
        migrations.RemoveField(
            model_name='newpair',
            name='social_2',
        ),
        migrations.AddField(
            model_name='newpair',
            name='profile1',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='profile1', to='searching.profile', verbose_name='Анкета отправителя'),
        ),
        migrations.AddField(
            model_name='newpair',
            name='profile2',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='profile2', to='searching.profile', verbose_name='Анкета получателя'),
        ),
        migrations.AddField(
            model_name='newpair',
            name='user1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newpair',
            name='user2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL, verbose_name='Получатель'),
            preserve_default=False,
        ),
    ]
