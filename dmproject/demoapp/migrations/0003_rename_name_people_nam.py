# Generated by Django 4.1.3 on 2022-11-17 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='nam',
        ),
    ]