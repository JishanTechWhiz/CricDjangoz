# Generated by Django 3.2.12 on 2024-03-26 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0009_boxground_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scorecard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tossWin', models.CharField(max_length=50)),
                ('battingTeam', models.CharField(max_length=50)),
                ('bowlingTeam', models.CharField(max_length=50)),
                ('firstInnings_totalRuns', models.IntegerField()),
                ('firstInnings_totalFours', models.IntegerField()),
                ('firstInnings_totalSixs', models.IntegerField()),
                ('firstInnings_totalWicket', models.IntegerField()),
                ('secondInnings_totalRuns', models.IntegerField()),
                ('secondInnings_totalFours', models.IntegerField()),
                ('secondInnings_totalSixs', models.IntegerField()),
                ('secondInnings_totalWicket', models.IntegerField()),
                ('winnerTeam', models.CharField(max_length=50)),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='scorecard', to='cricss.match')),
            ],
        ),
    ]
