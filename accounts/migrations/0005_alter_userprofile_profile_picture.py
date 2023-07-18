# Generated by Django 4.2.2 on 2023-07-18 23:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="userprofile/default_profile_picture.jpg",
                upload_to="userprofile",
            ),
        ),
    ]
