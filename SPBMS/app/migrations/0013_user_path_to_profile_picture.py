# Generated by Django 4.2.3 on 2023-11-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_budeget_end_date_budeget_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='path_to_profile_picture',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
