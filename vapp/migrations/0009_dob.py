# Generated by Django 3.2.9 on 2021-11-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0008_alter_task_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='dob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateTimeField()),
            ],
        ),
    ]
