# Generated by Django 3.2.9 on 2021-11-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0009_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dob',
            name='dob',
            field=models.DateField(),
        ),
    ]
