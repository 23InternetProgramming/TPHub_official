# Generated by Django 3.1.1 on 2023-11-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0006_merge_20231127_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
