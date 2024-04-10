# Generated by Django 4.1 on 2024-04-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_controllermodel_id_alter_dataplanemodel_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="controllermodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="dataplanemodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="devicemodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
