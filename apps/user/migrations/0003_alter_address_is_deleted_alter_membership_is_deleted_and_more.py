# Generated by Django 4.2.1 on 2023-06-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_address_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userrewardlog',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]