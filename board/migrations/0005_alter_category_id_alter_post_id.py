# Generated by Django 4.2.7 on 2023-11-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_merge_20231124_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
