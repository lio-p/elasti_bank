# Generated by Django 3.1.2 on 2020-10-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20201023_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentitem',
            name='featured',
            field=models.BooleanField(default=0),
        ),
    ]
