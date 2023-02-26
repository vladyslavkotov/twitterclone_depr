# Generated by Django 4.1.6 on 2023-02-26 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='link',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='email'),
        ),
    ]