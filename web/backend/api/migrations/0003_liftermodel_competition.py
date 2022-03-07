# Generated by Django 4.0.3 on 2022-03-05 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_event_name_competitionmodel_competition_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="liftermodel",
            name="competition",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.competitionmodel",
            ),
            preserve_default=False,
        ),
    ]
