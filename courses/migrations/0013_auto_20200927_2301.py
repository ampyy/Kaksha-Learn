# Generated by Django 3.1 on 2020-09-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200927_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preview',
            old_name='head',
            new_name='head1',
        ),
        migrations.RenameField(
            model_name='preview',
            old_name='iframe',
            new_name='iframe1',
        ),
        migrations.AddField(
            model_name='preview',
            name='head2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preview',
            name='head3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preview',
            name='iframe2',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preview',
            name='iframe3',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
