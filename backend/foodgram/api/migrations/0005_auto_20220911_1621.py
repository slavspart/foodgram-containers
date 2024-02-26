# Generated by Django 2.2.19 on 2022-09-11 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220911_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipetag',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Tag'),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='api.RecipeIngredient', to='api.Ingredient'),
        ),
    ]
