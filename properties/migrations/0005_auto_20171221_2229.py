# Generated by Django 2.0 on 2017-12-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20171221_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='bathroom_img',
            field=models.ImageField(upload_to='static'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='bedroom_img',
            field=models.ImageField(upload_to='static'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='house_img',
            field=models.ImageField(upload_to='static'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='sitting_room_img',
            field=models.ImageField(upload_to='static'),
        ),
    ]
