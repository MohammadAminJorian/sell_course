# Generated by Django 4.2 on 2023-04-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_course_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='timeofcourse',
            field=models.CharField(default=1, max_length=29),
            preserve_default=False,
        ),
    ]
