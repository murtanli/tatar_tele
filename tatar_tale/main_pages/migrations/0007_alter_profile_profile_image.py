# Generated by Django 5.0.6 on 2024-05-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles_image/'),
        ),
    ]