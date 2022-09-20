from django.urls import path

from viewer.views import TeamCreateView, TeamsView, TeamDeleteView, TournamentsView

app_name = 'viewer'
urlpatterns = [
    path('', TournamentsView.as_view(), name="index"),
    path('create_team', TeamCreateView.as_view(), name="create_team"),
    path('teams', TeamsView.as_view(), name="teams"),
    path('team/<int:pk>/delete', TeamDeleteView.as_view(), name="delete_team"),
]