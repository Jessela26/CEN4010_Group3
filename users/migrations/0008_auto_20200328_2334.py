# Generated by Django 3.0.3 on 2020-03-28 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default='33199', max_length=5),
        ),
    ]
