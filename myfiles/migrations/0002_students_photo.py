# Generated by Django 5.1.2 on 2024-12-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/photos/'),
        ),
    ]
