# Generated by Django 3.2 on 2022-01-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashcall', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='Bill_Investor',
            new_name='Investor_ID',
        ),
        migrations.RenameField(
            model_name='invoices',
            old_name='Invoice_Investor',
            new_name='Investor_ID',
        ),
    ]
