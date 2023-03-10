# Generated by Django 4.1.5 on 2023-01-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=250)),
                ('team_image', models.ImageField(upload_to='pics2')),
                ('team_desc', models.TextField()),
            ],
        ),
    ]
