# Generated by Django 3.1.1 on 2023-11-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]