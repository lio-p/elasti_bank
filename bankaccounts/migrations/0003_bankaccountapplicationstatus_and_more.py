# Generated by Django 4.1.7 on 2023-03-14 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0002_bankaccountapplications'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccountApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusname', models.CharField(max_length=56, verbose_name='Bank account application status')),
            ],
        ),
        migrations.AlterField(
            model_name='bankaccountapplications',
            name='country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccountapplications',
            name='province',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccountapplications',
            name='streetaddress1',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccountapplications',
            name='streetaddress2',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankaccountapplications',
            name='suburb',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='bankaccountapplications',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bankaccounts.bankaccountapplicationstatus'),
            preserve_default=False,
        ),
    ]
