# Generated by Django 3.2.9 on 2021-11-16 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20211116_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
