# Generated by Django 4.1.7 on 2023-03-16 00:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0002_alter_animal_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
