# Generated by Django 4.0.2 on 2022-02-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelAppp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='capacity',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.CharField(max_length=20),
        ),
    ]
