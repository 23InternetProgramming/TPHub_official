# Generated by Django 3.1.1 on 2023-12-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_profile', '0015_alter_post_id_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
