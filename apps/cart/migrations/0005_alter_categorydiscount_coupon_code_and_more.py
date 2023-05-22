# Generated by Django 4.2.1 on 2023-05-22 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0004_alter_categorydiscount_coupon_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorydiscount",
            name="coupon_code",
            field=models.CharField(
                default="79B72",
                editable=False,
                max_length=50,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="orderinfo",
            name="order_id",
            field=models.UUIDField(
                default=uuid.UUID("bb1e601a-a570-4469-b286-6996076891f8"),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="productdiscount",
            name="coupon_code",
            field=models.CharField(
                default="79B72",
                editable=False,
                max_length=50,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]