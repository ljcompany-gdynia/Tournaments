from django.contrib.auth.models import User
from django.db import models
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="team_pics")

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    name = models.CharField(max_length=40)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(default="player_pics/avatar.png", upload_to='player_pics')
    def __str__(self):
        return f'{self.name}'


class Tournament(models.Model):
    players = models.ManyToManyField(Player, blank=True, null=True)

