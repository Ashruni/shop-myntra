# Generated by Django 4.1 on 2023-02-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0025_wishlist_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='uc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
