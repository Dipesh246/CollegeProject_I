# Generated by Django 4.2.3 on 2023-11-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_user_path_to_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='allocated_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
