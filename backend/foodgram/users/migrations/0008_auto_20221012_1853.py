# Generated by Django 2.2.16 on 2022-10-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20221011_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_surbscribed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
