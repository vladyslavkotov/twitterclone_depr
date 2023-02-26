# Generated by Django 4.1.6 on 2023-02-26 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweet',
            name='replied_to',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='replied_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
