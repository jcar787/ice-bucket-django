from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ['first_name', 'last_name', 'profession', 'youtube_video', 'date_did_challenge']
		widgets = {'date_did_challenge': forms.DateInput(attrs={'class': 'datepicker'})}