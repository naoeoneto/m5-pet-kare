# Generated by Django 4.1.6 on 2023-02-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="sex",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Not Informed", "Default"),
                ],
                default="Not Informed",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="weight",
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
