# Generated by Django 3.2.12 on 2024-04-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0011_delete_tournamentteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.CharField(default='', max_length=50)),
                ('Players', models.ManyToManyField(to='cricss.User')),
                ('tournamentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricss.tournament')),
            ],
        ),
    ]
