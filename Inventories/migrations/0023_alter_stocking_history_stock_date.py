# Generated by Django 4.1.1 on 2022-11-29 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0022_alter_stocking_history_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocking_history',
            name='stock_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 13, 25, 29, 614185, tzinfo=datetime.timezone.utc)),
        ),
    ]