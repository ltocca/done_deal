# Generated by Django 4.1 on 2023-06-12 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("listing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
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
                ("name", models.CharField(max_length=128)),
            ],
            options={
                "verbose_name_plural": "Regions",
                "ordering": ("name",),
            },
        ),
        migrations.AddField(
            model_name="listing",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="listings",
                to="listing.category",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="listings",
                to="listing.region",
            ),
        ),
    ]