# Generated by Django 5.0.7 on 2024-08-10 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0004_alter_shorteneurls_prefix_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="shorteneurls",
            name="click",
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="Statistic",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("ip", models.CharField(max_length=15)),
                ("web_browser", models.CharField(max_length=50)),
                (
                    "device",
                    models.CharField(
                        choices=[
                            ("pc", "Pc"),
                            ("mobile", "Mobile"),
                            ("tablet", "Tablet"),
                        ],
                        max_length=6,
                    ),
                ),
                ("device_os", models.CharField(max_length=30)),
                ("country_code", models.CharField(default="XX", max_length=2)),
                ("country_name", models.CharField(default="Unknown", max_length=50)),
                (
                    "shortened_url",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shortener.shorteneurls",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
