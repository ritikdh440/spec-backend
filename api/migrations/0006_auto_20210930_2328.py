# Generated by Django 3.2.7 on 2021-09-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20210930_1636"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccessModel",
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
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="alumni",
            name="profile_pic_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="blog",
            name="cover_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="gallery",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="teammodel",
            name="profile_pic_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="workshop",
            name="cover_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
