# Generated by Django 4.1 on 2023-01-30 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regshopmodels',
            old_name='confirmpassword',
            new_name='confirmpass',
        ),
    ]
