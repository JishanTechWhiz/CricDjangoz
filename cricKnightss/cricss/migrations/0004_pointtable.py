# Generated by Django 3.2.12 on 2024-03-03 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricss', '0003_auto_20240303_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName1', models.CharField(max_length=30)),
                ('matches1', models.IntegerField()),
                ('win1', models.IntegerField()),
                ('loss1', models.IntegerField()),
                ('tie1', models.IntegerField()),
                ('teamName2', models.CharField(max_length=30)),
                ('matches2', models.IntegerField()),
                ('win2', models.IntegerField()),
                ('loss2', models.IntegerField()),
                ('tie2', models.IntegerField()),
                ('teamName3', models.CharField(max_length=30)),
                ('matches3', models.IntegerField()),
                ('win3', models.IntegerField()),
                ('loss3', models.IntegerField()),
                ('tie3', models.IntegerField()),
                ('teamName4', models.CharField(max_length=30)),
                ('matches4', models.IntegerField()),
                ('win4', models.IntegerField()),
                ('loss4', models.IntegerField()),
                ('tie4', models.IntegerField()),
                ('teamName5', models.CharField(max_length=30)),
                ('matches5', models.IntegerField()),
                ('win5', models.IntegerField()),
                ('loss5', models.IntegerField()),
                ('tie5', models.IntegerField()),
                ('teamName6', models.CharField(max_length=30)),
                ('matches6', models.IntegerField()),
                ('win6', models.IntegerField()),
                ('loss6', models.IntegerField()),
                ('tie6', models.IntegerField()),
                ('tournamentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cricss.tournament')),
            ],
        ),
    ]
