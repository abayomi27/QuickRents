# Generated by Django 2.0 on 2017-12-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
