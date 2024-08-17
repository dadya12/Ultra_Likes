# Generated by Django 5.0.6 on 2024-08-17 08:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_articlelike_commentlike'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='users_likes',
            field=models.ManyToManyField(related_name='users_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='users_likes',
            field=models.ManyToManyField(related_name='users_likes_com', to=settings.AUTH_USER_MODEL),
        ),
    ]
