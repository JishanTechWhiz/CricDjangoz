# Generated by Django 3.2.12 on 2024-04-10 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0014_boxground_organizername'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricss.user'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricss.user'),
        ),
    ]
