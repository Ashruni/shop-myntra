# Generated by Django 4.1 on 2023-02-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0007_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='bagmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
                ('productprice', models.IntegerField()),
                ('productdescription', models.CharField(max_length=150)),
                ('productfile', models.ImageField(upload_to='')),
            ],
        ),
    ]