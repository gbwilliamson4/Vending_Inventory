# Generated by Django 4.1.1 on 2022-09-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0009_needed_inventory_admin_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='needed_inventory',
            options={'verbose_name_plural': 'Needed Inventory'},
        ),
        migrations.AlterModelOptions(
            name='purchase_history',
            options={'verbose_name_plural': 'Purchase History'},
        ),
        migrations.RemoveField(
            model_name='needed_inventory',
            name='pending',
        ),
        migrations.AlterField(
            model_name='purchase_history',
            name='purchase_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]