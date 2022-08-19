# Generated by Django 4.0.6 on 2022-08-08 01:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("models", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Flower",
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
                ("count", models.IntegerField(blank=True, default=0, null=True)),
                ("description", models.TextField(null=True)),
                ("delivered_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("could_use_in_bouquet", models.BooleanField(default=True, null=True)),
                (
                    "wikipedia",
                    models.URLField(
                        default="https://www.wikipedia.org/",
                        null=True,
                        unique_for_date="delivered_at",
                    ),
                ),
                ("name", models.CharField(max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("second_email", models.EmailField(max_length=254, null=True)),
                ("name", models.CharField(max_length=64, null=True)),
                ("invoice", models.FileField(null=True, upload_to="uploads/%Y/%m/%d/")),
                ("user_uuid", models.UUIDField(editable=False, null=True)),
                (
                    "discount_size",
                    models.DecimalField(decimal_places=5, max_digits=5, null=True),
                ),
                (
                    "client_ip",
                    models.GenericIPAddressField(
                        blank=True, null=True, protocol="IPv4"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bouquet",
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
                (
                    "fresh_period",
                    models.DurationField(
                        default=datetime.timedelta(days=5),
                        help_text="Use this field when you need to have information about bouquet fresh time",
                        null=True,
                    ),
                ),
                ("photo", models.ImageField(blank=True, null=True, upload_to="")),
                ("price", models.FloatField(default=1.0, null=True)),
                (
                    "flowers",
                    models.ManyToManyField(
                        to="models.flower",
                        verbose_name="This bouquet consists of this flowers",
                    ),
                ),
            ],
            managers=[
                ("shop", django.db.models.manager.Manager()),
            ],
        ),
    ]
