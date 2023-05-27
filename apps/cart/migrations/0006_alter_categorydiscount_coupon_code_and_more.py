# Generated by Django 4.2.1 on 2023-05-26 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_categorydiscount_coupon_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydiscount',
            name='coupon_code',
            field=models.CharField(default='583CD', editable=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('ea2ab8a8-7c62-4a76-89b5-041313178de9'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='coupon_code',
            field=models.CharField(default='583CD', editable=False, max_length=50, unique=True),
        ),
    ]
