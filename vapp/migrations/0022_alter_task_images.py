# Generated by Django 3.2.9 on 2021-11-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0021_alter_task_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Images',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
    ]