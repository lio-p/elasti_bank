# Generated by Django 4.1.7 on 2023-03-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_remove_debittransactions_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='credittransactions',
            name='description',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='credittransactions',
            name='reference',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debittransactions',
            name='description',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debittransactions',
            name='reference',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
