# Generated by Django 4.1.7 on 2023-05-27 10:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0007_alter_recipe_in_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='favorited',
            field=models.ManyToManyField(blank=True, help_text='Избранное', related_name='favorited_recipes', to=settings.AUTH_USER_MODEL, verbose_name='Избранное'),
        ),
    ]
