# Generated by Django 3.2.12 on 2024-04-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0012_tourteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourteam',
            name='Captain_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
