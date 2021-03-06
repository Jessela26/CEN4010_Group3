# Generated by Django 3.0.3 on 2020-03-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=30)),
                ('address_2', models.CharField(max_length=50)),
                ('city', models.CharField(default='Miami', max_length=60)),
                ('state', models.CharField(default='Florida', max_length=30)),
                ('zip_code', models.CharField(default='33129', max_length=5)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
