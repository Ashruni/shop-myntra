# Generated by Django 4.1 on 2023-02-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myntraapp', '0012_rename_customercardpay_customercard'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerlocationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('locality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
    ]
