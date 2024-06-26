# Generated by Django 3.2.12 on 2024-03-03 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchScorerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tossWin', models.CharField(max_length=30)),
                ('battingTeam', models.CharField(max_length=30)),
                ('bowlingTeam', models.CharField(max_length=30)),
                ('firstInnings_totalRuns', models.IntegerField()),
                ('firstInnings_totalFours', models.IntegerField()),
                ('firstInnings_totalSixs', models.IntegerField()),
                ('firstInnings_totalWicket', models.IntegerField()),
                ('secondInnings_totalRuns', models.IntegerField()),
                ('secondInnings_totalFours', models.IntegerField()),
                ('secondInnings_totalSixs', models.IntegerField()),
                ('secondInnings_totalWicket', models.IntegerField()),
                ('winnerTeam', models.CharField(max_length=30)),
                ('matchId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricss.match')),
                ('teamId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricss.team')),
            ],
        ),
        migrations.DeleteModel(
            name='ScorerDetail',
        ),
    ]
