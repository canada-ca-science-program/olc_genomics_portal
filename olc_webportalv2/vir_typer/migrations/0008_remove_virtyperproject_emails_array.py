# Generated by Django 2.1.5 on 2019-07-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0007_auto_20190730_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtyperproject',
            name='emails_array',
        ),
    ]
