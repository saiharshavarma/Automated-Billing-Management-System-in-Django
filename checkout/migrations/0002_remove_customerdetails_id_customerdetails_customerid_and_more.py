# Generated by Django 4.0.3 on 2022-04-10 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0008_usercart_quantity'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='id',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='customerid',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Medicine_Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkout.customerdetails')),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.itemmain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]