# Generated by Django 3.2.12 on 2024-03-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0007_remove_tournament_bannerimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxground',
            name='boxImg',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='boxground',
            name='rating',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
