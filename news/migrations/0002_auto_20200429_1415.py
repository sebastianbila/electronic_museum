# Generated by Django 3.0.5 on 2020-04-29 14:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
