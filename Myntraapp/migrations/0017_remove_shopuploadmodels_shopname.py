# Generated by Django 4.1 on 2023-02-17 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0016_shopuploadmodels_shopname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuploadmodels',
            name='shopname',
        ),
    ]
