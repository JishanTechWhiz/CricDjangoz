# Generated by Django 3.2.12 on 2024-03-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0008_auto_20240324_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxground',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]