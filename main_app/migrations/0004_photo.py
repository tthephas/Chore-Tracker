# Generated by Django 4.1.7 on 2023-03-12 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_kid_chores"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=200)),
                (
                    "kid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main_app.kid"
                    ),
                ),
            ],
        ),
    ]
