# Generated by Django 3.2.9 on 2021-11-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_delete_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]