# Generated by Django 4.2.11 on 2024-04-11 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stock",
            field=models.IntegerField(default=0),
        ),
    ]
