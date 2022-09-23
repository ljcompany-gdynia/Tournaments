from django.forms import ModelForm

from viewer.models import Team, Player, Tournament


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'user_id': 'User',
            'name': 'Nazwa',
            'image': 'Zdjęcie',
        }


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'avatar': 'Zdjęcie',
        }


class TournamentForm(ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
