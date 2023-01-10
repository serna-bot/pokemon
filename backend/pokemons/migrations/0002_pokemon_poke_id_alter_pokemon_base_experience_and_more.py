# Generated by Django 4.1.5 on 2023-01-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='poke_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='base_experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
