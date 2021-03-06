# Generated by Django 3.1 on 2020-08-30 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('course_bought', models.CharField(max_length=50)),
                ('amount_payable', models.PositiveIntegerField()),
                ('paid', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='No', max_length=10)),
            ],
        ),
    ]
