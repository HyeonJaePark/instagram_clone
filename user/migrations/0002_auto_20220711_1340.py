# Generated by Django 3.2.12 on 2022-07-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]
