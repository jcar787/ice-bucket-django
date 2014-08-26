from django.conf.urls import patterns, include, url, handler404
from .views import ParticipantFormView, ParticipantDetailView, ParticipantListView, Template404View

urlpatterns = patterns('', 
	url(r'^$', ParticipantListView.as_view()),
	url(r'^list/$', ParticipantListView.as_view()),
	url(r'^new/$', ParticipantFormView.as_view()),
	url(r'^success/(?P<pk>\d+)/$', ParticipantDetailView.as_view()),
	url(r'^detail/(?P<pk>\d+)/$', ParticipantDetailView.as_view(), name='participant_detail'),
	url(r'^error/$', Template404View.as_view()),
)
handler404 = Template404View.as_view()