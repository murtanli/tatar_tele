# Generated by Django 5.0.6 on 2024-05-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talesinfo',
            name='percent_progress',
            field=models.IntegerField(default=0),
        ),
    ]
