# Generated by Django 4.2 on 2024-01-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_auto_20200829_1454"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
