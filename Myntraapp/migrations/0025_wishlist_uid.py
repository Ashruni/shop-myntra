# Generated by Django 4.1 on 2023-02-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0024_remove_shopuploadmodels_userid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]