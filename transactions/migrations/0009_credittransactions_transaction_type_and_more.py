# Generated by Django 4.1.7 on 2023-03-23 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_credittransactiontype_debittransactiontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='credittransactions',
            name='transaction_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.credittransactiontype'),
        ),
        migrations.AddField(
            model_name='debittransactions',
            name='transaction_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.debittransactiontype'),
        ),
    ]
