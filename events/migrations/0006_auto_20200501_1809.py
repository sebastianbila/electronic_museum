# Generated by Django 3.0.5 on 2020-05-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20200501_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='', max_length=850),
        ),
    ]
