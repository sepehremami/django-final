# Generated by Django 4.2.1 on 2023-05-20 20:33

import apps.shop.models
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import profanity.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "Available"), ("U", "Unavailable")],
                        default="U",
                        max_length=3,
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        editable=False,
                        max_digits=10,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("quantity", models.SmallIntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "desc",
                    models.TextField(
                        validators=[profanity.validators.validate_is_profane]
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="images")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("img", models.ImageField(blank=True, null=True, upload_to="images")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("name", models.CharField(max_length=150)),
                (
                    "desc",
                    models.TextField(
                        validators=[profanity.validators.validate_is_profane]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductColour",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("colour", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SubProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("sku", models.CharField(max_length=100)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("s", "Small"),
                            ("m", "Medium"),
                            ("l", "Large"),
                            ("xl", "Extra-Large"),
                            ("xxl", "2Extra-Large"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "colour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="shop.productcolour",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shop.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                (
                    "rating",
                    models.DecimalField(
                        decimal_places=0,
                        max_digits=5,
                        validators=[apps.shop.models.validate_max_five],
                    ),
                ),
                ("text", models.CharField(max_length=200)),
                (
                    "parent_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.productreview",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
