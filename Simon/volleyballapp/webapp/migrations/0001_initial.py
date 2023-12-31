# Generated by Django 4.2.6 on 2023-10-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField()),
                ('match_location', models.CharField(max_length=200)),
                ('match_result', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=200)),
                ('player_surname', models.CharField(max_length=200)),
                ('player_nickname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='rounds',
            fields=[
                ('round_id', models.AutoField(primary_key=True, serialize=False)),
                ('round_name', models.CharField(max_length=200)),
                ('round_result', models.CharField(max_length=200)),
                ('round_date', models.DateField()),
                ('round_time', models.TimeField()),
                ('round_matches', models.ManyToManyField(to='webapp.matches')),
            ],
        ),
        migrations.CreateModel(
            name='tournaments',
            fields=[
                ('tournament_id', models.AutoField(primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(max_length=200)),
                ('tournament_result', models.CharField(max_length=200)),
                ('tournament_date', models.DateField()),
                ('tournament_time', models.TimeField()),
                ('tournament_location', models.CharField(max_length=200)),
                ('tournament_city', models.CharField(max_length=200)),
                ('tournament_match', models.ManyToManyField(to='webapp.matches')),
                ('tournament_rounds', models.ManyToManyField(to='webapp.rounds')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=200)),
                ('team_city', models.CharField(max_length=200)),
                ('team_country', models.CharField(max_length=200)),
                ('team_members', models.ManyToManyField(to='webapp.players')),
            ],
        ),
        migrations.AddField(
            model_name='rounds',
            name='round_teams',
            field=models.ManyToManyField(to='webapp.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='match_teams',
            field=models.ManyToManyField(to='webapp.teams'),
        ),
    ]
