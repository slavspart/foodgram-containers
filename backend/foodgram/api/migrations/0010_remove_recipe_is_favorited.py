# Generated by Django 2.2.19 on 2022-09-16 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_favorite_favoriteadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='is_favorited',
        ),
    ]
