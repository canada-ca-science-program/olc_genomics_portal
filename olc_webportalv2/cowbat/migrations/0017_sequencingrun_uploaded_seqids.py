# Generated by Django 2.1.5 on 2019-09-11 15:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowbat', '0016_sequencingrun_seqids_to_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequencingrun',
            name='uploaded_seqids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True, default=list, size=None),
        ),
    ]