# Generated by Django 4.2.1 on 2023-05-18 23:07

import apps.shop.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_alter_productreview_parent_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productreview",
            name="rating",
            field=models.DecimalField(
                decimal_places=0,
                max_digits=5,
                validators=[apps.shop.models.validate_max_five],
            ),
        ),
    ]
