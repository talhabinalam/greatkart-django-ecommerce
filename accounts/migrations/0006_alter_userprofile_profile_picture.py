# Generated by Django 4.2.2 on 2023-07-19 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_alter_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="userprofile/default_profile_picture.jpg",
                null=True,
                upload_to="userprofile/",
            ),
        ),
    ]
