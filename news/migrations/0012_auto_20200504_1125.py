# Generated by Django 3.0.5 on 2020-05-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20200429_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
