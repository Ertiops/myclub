# Generated by Django 4.1.6 on 2023-07-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
