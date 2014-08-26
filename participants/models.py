from django.db import models

# Create your models here.
class Participant(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	profession = models.CharField(max_length=25)
	youtube_video = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now=True)
	date_did_challenge = models.DateField(null=True)

	class Meta:
		ordering = ['last_name']

	def __str__(self):
		return '{0}, {1}'.format(self.last_name, self.first_name)

	def __unicode__(self):
		return u'{0}, {1}'.format(self.last_name, self.first_name)		