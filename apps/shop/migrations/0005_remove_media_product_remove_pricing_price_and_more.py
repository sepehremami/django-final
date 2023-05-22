# Generated by Django 4.2.1 on 2023-05-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_media_name_media_subproduct_alter_category_parent_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="media",
            name="product",
        ),
        migrations.RemoveField(
            model_name="pricing",
            name="price",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="media",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="media/media"),
        ),
    ]