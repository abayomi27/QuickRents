# Generated by Django 2.0 on 2017-12-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20171220_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='price',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
    ]
