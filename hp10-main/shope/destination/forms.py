from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name','location', 'description','image','featured_activities','best_time_to_visit']