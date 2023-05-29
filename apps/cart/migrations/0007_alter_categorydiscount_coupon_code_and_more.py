# Generated by Django 4.2.1 on 2023-05-29 23:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_categorydiscount_coupon_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydiscount',
            name='coupon_code',
            field=models.CharField(default='44B03', editable=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('38a756a5-6de6-46f1-8d82-2de135f8b675'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='coupon_code',
            field=models.CharField(default='44B03', editable=False, max_length=50, unique=True),
        ),
    ]