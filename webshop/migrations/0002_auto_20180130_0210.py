# Generated by Django 2.0 on 2018-01-30 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vat_info',
            name='country_name',
        ),
        migrations.AddField(
            model_name='vat_info',
            name='country_id',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
