from django.forms.util import ErrorList
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView
from .forms import ParticipantForm
from .models import Participant
from datetime import datetime


# Create your views here.
class ParticipantFormView(FormView):
	template_name = 'participant_form.html'
	form_class = ParticipantForm

	def form_invalid(self, form):
		return super(ParticipantFormView, self).form_invalid(form)

	def form_valid(self, form):
		participant = form.save(commit=False)
		tmp = participant.youtube_video.split('?')

		if len(tmp) > 1 and tmp[1][0] == 'v':
			participant.youtube_video = tmp[1].split('=')[1]
		else:
			errors = form._errors.setdefault("youtube_video", ErrorList())
			errors.append(u"Not a youtube video")
			return self.form_invalid(form)
		
		participant.save()
		self.success_url = '/success/{0}'.format(participant.id)
		return super(ParticipantFormView, self).form_valid(form)


class ParticipantDetailView(DetailView):
	template_name = 'participant_detail.html'
	model = Participant

	def get_context_data(self, **kwargs):
		return super(ParticipantDetailView, self).get_context_data(**kwargs)


class ParticipantListView(ListView):
	template_name = 'participant_list.html'
	paginate_by = 9
	model = Participant

class Template404View(TemplateView):
	template_name = '404.html'