# Generated by Django 4.1 on 2023-01-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0003_shopuploadmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuploadmodels',
            name='productfile',
            field=models.ImageField(upload_to='Myntraapp/static'),
        ),
    ]
