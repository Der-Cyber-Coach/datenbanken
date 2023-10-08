from django.db import models

# Create your models here.

class Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=200)
    player_surname = models.CharField(max_length=200)
    player_nickname = models.CharField(max_length=200)
    
    
class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=200)
    team_city = models.CharField(max_length=200)
    team_country = models.CharField(max_length=200)
    team_members = models.ManyToManyField(Players)
    


class Matches(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_date = models.DateField()
    match_time = models.TimeField()
    match_location = models.CharField(max_length=200)
    match_teams = models.ManyToManyField(Teams)
    match_result = models.CharField(max_length=200)

class rounds(models.Model):
    round_id = models.AutoField(primary_key=True)
    round_name = models.CharField(max_length=200)
    round_matches = models.ManyToManyField(Matches)
    round_teams = models.ManyToManyField(Teams)
    round_result = models.CharField(max_length=200)
    round_date = models.DateField()
    round_time = models.TimeField()
    
    
class tournaments(models.Model):
    tournament_id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=200)
    tournament_rounds = models.ManyToManyField(rounds)
    tournament_result = models.CharField(max_length=200)
    tournament_date = models.DateField()
    tournament_time = models.TimeField()
    tournament_location = models.CharField(max_length=200)
    tournament_city = models.CharField(max_length=200)
    tournament_match = models.ManyToManyField(Matches)