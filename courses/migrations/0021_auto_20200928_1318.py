# Generated by Django 3.1 on 2020-09-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20200928_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='number',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
