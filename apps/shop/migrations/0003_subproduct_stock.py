# Generated by Django 4.2.1 on 2023-06-02 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproduct',
            name='stock',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
