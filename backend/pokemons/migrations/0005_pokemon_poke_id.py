# Generated by Django 4.1.5 on 2023-01-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0004_remove_pokemon_poke_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='poke_id',
            field=models.IntegerField(default=-1),
        ),
    ]