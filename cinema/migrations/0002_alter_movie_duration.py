# Generated by Django 4.2.7 on 2023-11-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
