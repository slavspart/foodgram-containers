# Generated by Django 2.2.19 on 2022-09-20 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_recipeingredient_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='measurment_unit',
            new_name='measurement_unit',
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='recipe_ingredients', to='api.Recipe'),
        ),
    ]