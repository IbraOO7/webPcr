# Generated by Django 3.1.3 on 2021-02-21 09:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('halaman', '0002_harga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tentang',
            name='brosur',
        ),
        migrations.RemoveField(
            model_name='tentang',
            name='client',
        ),
        migrations.AddField(
            model_name='tentang',
            name='text_tentang',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]