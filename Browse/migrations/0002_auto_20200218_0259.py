# Generated by Django 3.0.3 on 2020-02-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year_published',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
