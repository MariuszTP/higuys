# Generated by Django 3.2.16 on 2022-12-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageb', '0011_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='name',
            field=models.CharField(max_length=5, null=True),
        ),
    ]