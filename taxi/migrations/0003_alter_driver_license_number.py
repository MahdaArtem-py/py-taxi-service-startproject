# Generated by Django 5.1.2 on 2024-10-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0002_alter_driver_license_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
