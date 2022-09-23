from django.urls import path

from viewer.views import TeamCreateView, TeamsView, TeamDeleteView, TournamentsIndexView, PlayerCreateView, PlayersView, \
    PlayerDeleteView, TournamentCreateView, TournamentsView

app_name = 'viewer'
urlpatterns = [
    path('', TournamentsIndexView.as_view(), name="index"),
    path('create_team', TeamCreateView.as_view(), name="create_team"),
    path('teams', TeamsView.as_view(), name="teams"),
    path('team/<int:pk>/delete', TeamDeleteView.as_view(), name="delete_team"),
    path('create_player', PlayerCreateView.as_view(), name="create_player"),
    path('players', PlayersView.as_view(), name="players"),
    path('player/<int:pk>/delete', PlayerDeleteView.as_view(), name="delete_player"),
    path('create_tournament', TournamentCreateView.as_view(), name="create_tournament"),
    path('tournaments', TournamentsView.as_view(), name="tournaments"),
]