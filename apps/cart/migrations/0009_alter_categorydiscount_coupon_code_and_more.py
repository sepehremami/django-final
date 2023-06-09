# Generated by Django 4.2.1 on 2023-06-02 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_categorydiscount_coupon_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydiscount',
            name='coupon_code',
            field=models.CharField(default='55B90', editable=False, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('1d926952-92d9-4eca-8c79-c4471d0d11dc'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='productdiscount',
            name='coupon_code',
            field=models.CharField(default='55B90', editable=False, max_length=50, unique=True),
        ),
    ]
