# Generated by Django 3.2.9 on 2021-11-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0002_alter_user_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Images',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
    ]
