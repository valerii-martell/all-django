# Generated by Django 4.0.6 on 2022-08-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("graphql_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="make",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="model",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
