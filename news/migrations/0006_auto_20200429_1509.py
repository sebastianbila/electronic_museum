# Generated by Django 3.0.5 on 2020-04-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200429_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(blank=True, upload_to='news/'),
        ),
    ]
