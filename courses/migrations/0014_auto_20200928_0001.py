# Generated by Django 3.1 on 2020-09-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20200927_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='number',
            field=models.PositiveIntegerField(),
        ),
    ]
