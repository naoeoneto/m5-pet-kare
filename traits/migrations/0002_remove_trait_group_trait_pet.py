# Generated by Django 4.1.6 on 2023-02-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0001_initial"),
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="group",
        ),
        migrations.AddField(
            model_name="trait",
            name="pet",
            field=models.ManyToManyField(related_name="pets", to="pets.pet"),
        ),
    ]
