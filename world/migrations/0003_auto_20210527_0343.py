# Generated by Django 3.2 on 2021-05-27 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
