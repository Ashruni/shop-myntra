# Generated by Django 4.1 on 2023-02-17 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0023_wishlist_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuploadmodels',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='userid',
        ),
    ]
