# Generated by Django 4.2.7 on 2023-11-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0003_merge_0002_auto_20231123_1842_0002_auto_20231124_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
