# Generated by Django 3.1 on 2020-08-30 09:18

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('title', models.CharField(max_length=22)),
                ('cour_desc', models.CharField(max_length=255)),
                ('cour_time', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
