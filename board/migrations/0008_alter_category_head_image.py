# Generated by Django 4.2.7 on 2023-11-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_category_head_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='head_image',
            field=models.ImageField(upload_to='board/category_images/%Y/%m/%d/'),
        ),
    ]