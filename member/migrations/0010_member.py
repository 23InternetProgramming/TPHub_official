# Generated by Django 3.1.1 on 2023-12-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_merge_20231202_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]