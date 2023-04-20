# Generated by Django 4.1.7 on 2023-04-06 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customuser_income_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='income_level',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='accounts.incomelevel'),
            preserve_default=False,
        ),
    ]
