# Generated by Django 2.2.16 on 2021-01-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(blank=True, max_length=254)),
                ("message", models.CharField(max_length=5000)),
                ("page_url", models.CharField(blank=True, max_length=2048)),
                ("creation_time", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]