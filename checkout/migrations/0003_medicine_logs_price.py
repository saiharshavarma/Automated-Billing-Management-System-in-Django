# Generated by Django 4.0.3 on 2022-04-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_customerdetails_id_customerdetails_customerid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine_logs',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
            preserve_default=False,
        ),
    ]
