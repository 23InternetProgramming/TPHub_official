# Generated by Django 4.2.7 on 2023-11-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0004_merge_0002_auto_20231123_1842_0003_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
