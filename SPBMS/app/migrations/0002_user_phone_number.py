# Generated by Django 4.2.3 on 2023-07-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, max_length=10, null=True),
        ),
    ]
