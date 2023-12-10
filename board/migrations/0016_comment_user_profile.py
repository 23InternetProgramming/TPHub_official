# Generated by Django 3.1.1 on 2023-12-09 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('self_profile', '0019_delete_post'),
        ('board', '0015_post_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='self_profile.userprofile'),
        ),
    ]