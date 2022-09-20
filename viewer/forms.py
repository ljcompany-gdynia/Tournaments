from django.forms import ModelForm

from viewer.models import Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            # 'user_id': 'User',
            'name': 'Nazwa',
            'image': 'Zdjęcie',
        }
