# Generated by Django 4.2.1 on 2023-05-17 06:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0006_alter_dummy_dummy_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shoppingsession",
            name="user",
        ),
        migrations.DeleteModel(
            name="CartItem",
        ),
        migrations.DeleteModel(
            name="ShoppingSession",
        ),
    ]
