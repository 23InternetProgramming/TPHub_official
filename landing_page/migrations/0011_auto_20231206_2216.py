# Generated by Django 3.1.1 on 2023-12-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0010_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
