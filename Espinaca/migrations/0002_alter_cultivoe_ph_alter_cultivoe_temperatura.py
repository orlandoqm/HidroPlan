# Generated by Django 4.1.7 on 2023-08-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espinaca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivoe',
            name='ph',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cultivoe',
            name='temperatura',
            field=models.CharField(max_length=50),
        ),
    ]
