# Generated by Django 4.1.5 on 2023-01-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_rename_desc_team_team_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_image',
            field=models.ImageField(upload_to='pics2'),
        ),
    ]
