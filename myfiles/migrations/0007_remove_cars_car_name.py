# Generated by Django 5.1.2 on 2024-12-15 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0006_alter_cars_car_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='car_name',
        ),
    ]
