# Generated by Django 3.2.4 on 2021-06-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20210613_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='profit',
            field=models.FloatField(blank=True, default=None),
        ),
    ]
