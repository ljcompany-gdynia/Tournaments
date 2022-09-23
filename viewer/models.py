from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField, ImageField, ForeignKey, DO_NOTHING, ManyToManyField, CharField


class Team(models.Model):
    name = CharField(max_length=40)
    image = ImageField(upload_to="team_pics")

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    name = TextField()
    team = ForeignKey(Team, on_delete=DO_NOTHING)
    avatar = ImageField(default="player_pics/avatar.png", upload_to='player_pics')


class Tournament(models.Model):
    players = ManyToManyField(Player, blank=True, null=True)
