# Generated by Django 3.2.16 on 2022-12-19 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pageb', '0015_auto_20221219_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='kategoria',
            new_name='category',
        ),
    ]