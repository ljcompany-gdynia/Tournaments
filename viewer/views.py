from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from viewer.forms import TeamForm
from viewer.models import Tournament, Team, Player


class TournamentsIndexView(ListView):
    template_name = "tournaments_index.html"
    model = Tournament


class TeamCreateView(CreateView):
    template_name = 'forms/form.html'
    form_class = TeamForm
    success_url = reverse_lazy('viewer:teams')


class TeamsView(ListView):
    template_name = "teams.html"
    model = Team
    paginate_by = 10


class TeamDeleteView(DeleteView):
    template_name = "forms/team_delete_form.html"
    model = Team
    success_url = reverse_lazy('viewer:teams')


class PlayerCreateView(CreateView):
    template_name = "forms/form.html"
    model = Player
    success_url = reverse_lazy('viewer:players')
    fields = '__all__'


class PlayersView(ListView):
    template_name = "players.html"
    model = Player
    paginate_by = 10


class PlayerDeleteView(DeleteView):
    template_name = "forms/team_delete_form.html"
    model = Player
    success_url = reverse_lazy('viewer:players')


class TournamentCreateView(CreateView):
    template_name = "forms/form.html"
    model = Tournament
    success_url = reverse_lazy('viewer:index')
    fields = '__all__'


class TournamentsView(ListView):
    template_name = "tournaments.html"
    model = Tournament
    paginate_by = 10
