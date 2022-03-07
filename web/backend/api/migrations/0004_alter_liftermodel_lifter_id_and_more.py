# Generated by Django 4.0.3 on 2022-03-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_liftermodel_competition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="liftermodel",
            name="lifter_id",
            field=models.AutoField(
                default=0, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="sessionmodel",
            name="session_id",
            field=models.AutoField(
                default=0, primary_key=True, serialize=False
            ),
        ),
    ]
