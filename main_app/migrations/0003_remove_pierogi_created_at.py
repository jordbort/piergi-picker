# Generated by Django 4.1.5 on 2023-01-26 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_pierogi_verified_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pierogi',
            name='created_at',
        ),
    ]