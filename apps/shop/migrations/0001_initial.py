# Generated by Django 4.2.1 on 2023-05-15 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import profanity.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "desc",
                    models.TextField(
                        validators=[profanity.validators.validate_is_profane]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Discount",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "desc",
                    models.TextField(
                        validators=[profanity.validators.validate_is_profane]
                    ),
                ),
                ("discount_percent", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShoppingSession",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("name", models.CharField(max_length=150)),
                (
                    "desc",
                    models.TextField(
                        validators=[profanity.validators.validate_is_profane]
                    ),
                ),
                ("sku", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="shop.category",
                    ),
                ),
                (
                    "discount",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="shop.discount",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("quantity", models.SmallIntegerField()),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.shoppingsession",
                    ),
                ),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT, to="shop.product"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_date", django_jalali.db.models.jDateField(auto_now_add=True)),
                ("modified_date", django_jalali.db.models.jDateField(auto_now=True)),
                ("session_id", models.CharField(max_length=500)),
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
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]