# Generated by Django 4.1.3 on 2022-12-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
