# Generated by Django 5.0.6 on 2024-05-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0005_remove_profile_tales_info_progress_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles_image/profile.png', null=True, upload_to='profiles_image/'),
        ),
    ]
