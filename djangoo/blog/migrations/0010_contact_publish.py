# Generated by Django 4.2 on 2023-05-07 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_myvipuser_myuser_is_vip'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
