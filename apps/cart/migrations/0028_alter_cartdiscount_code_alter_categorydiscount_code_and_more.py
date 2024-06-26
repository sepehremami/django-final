# Generated by Django 4.2.1 on 2024-01-14 02:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0027_categorydiscount_code_productdiscount_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartdiscount",
            name="code",
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name="categorydiscount",
            name="code",
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name="orderinfo",
            name="order_id",
            field=models.UUIDField(
                default=uuid.UUID("577f3a00-7d17-49aa-a262-72e2f3cb2cca"),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="productdiscount",
            name="code",
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
