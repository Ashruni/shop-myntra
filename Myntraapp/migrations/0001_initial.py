# Generated by Django 4.1 on 2023-01-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regshopmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=30)),
                ('shoploc', models.CharField(max_length=30)),
                ('shopid', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mobnum', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
                ('confirmpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
