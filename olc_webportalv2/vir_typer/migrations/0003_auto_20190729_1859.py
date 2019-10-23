# Generated by Django 2.1.5 on 2019-07-29 18:59

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0002_auto_20190726_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirTyperFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_files', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), blank=True, default=[], size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='virtyperrequest',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vir_typer_project', to='vir_typer.VirTyperProject'),
        ),
        migrations.AddField(
            model_name='virtyperfiles',
            name='sample_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vir_typer_sample', to='vir_typer.VirTyperRequest'),
        ),
    ]
