# Generated by Django 3.1.1 on 2023-12-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_profile', '0012_auto_20231204_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='git',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
    ]