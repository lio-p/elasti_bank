# Generated by Django 4.1.7 on 2023-03-15 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0006_alter_bankaccountapplications_province'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='datetime',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='bankaccountapplications',
            old_name='datetime',
            new_name='created_at',
        ),
    ]
