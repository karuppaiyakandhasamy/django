# Generated by Django 3.2.9 on 2021-11-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Images',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='pics/', width_field=300),
        ),
    ]