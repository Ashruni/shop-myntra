# Generated by Django 4.1 on 2023-01-31 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0002_rename_confirmpassword_regshopmodels_confirmpass'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopuploadmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
                ('productprice', models.IntegerField()),
                ('productdescription', models.CharField(max_length=150)),
                ('productfile', models.FileField(upload_to='myapp/static')),
            ],
        ),
    ]
